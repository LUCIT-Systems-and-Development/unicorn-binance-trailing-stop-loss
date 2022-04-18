#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unicorn_binance_trailing_stop_loss/manager.py
#
# Part of ‘UNICORN Binance Trailing Stop Loss’
# Project website: https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
# Documentation: https://unicorn-binance-trailing-stop-loss.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-trailing-stop-loss
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


from unicorn_binance_rest_api.manager import BinanceRestApiManager
from unicorn_binance_rest_api.exceptions import BinanceAPIException
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
from unicorn_binance_websocket_api.exceptions import UnknownExchange, StreamRecoveryError
from typing import Optional
import datetime
import logging
import math
import smtplib
import requests
import ssl
import threading
import time


class BinanceTrailingStopLossManager:
    """
    unicorn-binance-trailing-stop-loss for managing Stop/Loss orders and sending notifications.

    Supported exchanges: binance.com-isolated_margin

    :param binance_public_key: Provide the public Binance key.
    :type binance_public_key: str
    :param binance_private_key: Provide the private Binance key.
    :type binance_private_key: str
    :param callback_error: Callback function used if an error occurs.
    :type callback_error: function
    :param callback_finished: Callback function used if stop_loss gets filled.
    :type callback_finished: function
    :param exchange: Choose the exchange endpoint: binance.com, binance.com-futures, binance.com-margin,
                     binance.com-isolated_margin
    :type exchange: str
    :param keep_threshold: If empty we sell the full balance, use integer or percent values.
    :type keep_threshold: str
    :param reset_stop_loss_price: Reset an existing stop_loss_price and calculate a new one. Only True is True, anything
                                  else is False!
    :type reset_stop_loss_price: bool
    :param stop_loss_limit: The limit is used to calculate the `stop_loss_price` of the highest given price, use integer
                            or percent values.
    :type stop_loss_limit: str
    :param send_to_email_address: Email address of receiver
    :type send_to_email_address: str
    :param send_from_email_address: Email address of sender
    :type send_from_email_address: str
    :param send_from_email_password: Password for SMTP auth
    :type send_from_email_password: str
    :param send_from_email_server: Hostname or IP of SMTP server
    :type send_from_email_server: str
    :param send_from_email_port: Port of SMTP server
    :type send_from_email_port: int
    :param stop_loss_market: The market to enforce stop/loss.
    :type stop_loss_market: str
    :param stop_loss_order_type: Can be `limit` or `market` - default is None which leads to a stop of the algorithm.
    :type stop_loss_order_type: str
    :param stop_loss_price: Set a price to use for stop/loss, this is valid till it get overwritten with a higher price.
    :type stop_loss_price: float
    :param stop_loss_side: Can be `buy` or `sell` - default is None which leads to a stop of the algorithm.
    :type stop_loss_side: str
    :param stop_loss_trigger_gap: Gap between stopPrice and limit order price, use integer or percent values.
    :type stop_loss_trigger_gap: str
    :param telegram_bot_token: Token to connect with Telegram API.
    :type telegram_bot_token: str
    :param telegram_send_to: Receiver of the message sent via Telegram.
    :type telegram_send_to: str
    :param trading_fee_use_bnb: Default is False. Set to True to use BNB for a discount on trading fees:
                                https://www.binance.com/en/support/faq/115000583311.
    :type trading_fee_use_bnb: bool
    """

    # Todo:
    #   - Precision dynamic
    #   - SELL/BUY
    #   - Notification if partially filled
    #   - Callback partial filled
    #   - Fees: how to handle? / VIP Fees
    #   - Exchanges
    #   - Notifications with missing parameters (exception handling)
    #   - use different callback functions for each stream within one ubwam instance

    def __init__(self,
                 binance_public_key: str = None,
                 binance_private_key: str = None,
                 callback_error: type(abs) = None,
                 callback_finished: type(abs) = None,
                 send_to_email_address: str = None,
                 send_from_email_address: str = None,
                 send_from_email_password: str = None,
                 send_from_email_server: str = None,
                 send_from_email_port: int = None,
                 exchange: str = "binance.com",
                 keep_threshold: str = None,
                 reset_stop_loss_price: bool = False,
                 stop_loss_limit: str = None,
                 stop_loss_market: str = None,
                 stop_loss_order_type: str = None,
                 stop_loss_price: float = None,
                 stop_loss_side: str = None,
                 stop_loss_trigger_gap: str = "0.01",
                 telegram_bot_token: str = None,
                 telegram_send_to: str = None,
                 trading_fee_discount_futures_percent: float = 10.0,
                 trading_fee_discount_margin_percent: float = 25.0,
                 trading_fee_discount_spot_percent: float = 25.0,
                 trading_fee_percent: float = 0.1,
                 trading_fee_use_bnb: bool = False):
        self.binance_public_key = binance_public_key
        self.binance_private_key = binance_private_key
        self.callback_error = callback_error
        self.callback_finished = callback_finished
        self.current_price: float = 0.0
        self.send_to_email_address = send_to_email_address
        self.send_from_email_address = send_from_email_address
        self.send_from_email_password = send_from_email_password
        self.send_from_email_server = send_from_email_server
        self.send_from_email_port = send_from_email_port
        self.exchange = exchange
        self.exchange_info: dict = {}
        self.keep_threshold = keep_threshold
        self.logger = logging.getLogger('unicorn_binance_trailing_stop_loss')
        self.precision_crypto: int = 2  # Todo: make dynamic
        self.precision_fiat: int = 2  # Todo: make dynamic
        self.reset_stop_loss_price = True if reset_stop_loss_price is True else False
        self.stop_loss_asset_name: str = ""
        self.stop_loss_asset_amount: float = 0.0
        self.stop_loss_asset_amount_free: float = 0.0
        self.stop_loss_limit = stop_loss_limit
        self.stop_loss_market = stop_loss_market
        self.stop_loss_order_id: int = 0
        self.stop_loss_order_type = stop_loss_order_type
        self.stop_loss_price: float = None if stop_loss_price is None else float(stop_loss_price)
        self.stop_loss_side = stop_loss_side
        self.stop_loss_quantity: float = 0.0
        self.stop_loss_trigger_gap = stop_loss_trigger_gap
        self.stop_loss_request: bool = False
        self.stop_request: bool = False
        self.symbol_info: dict = {}
        self.telegram_bot_token = telegram_bot_token
        self.telegram_send_to = telegram_send_to
        self.trading_fee_discount_futures_percent = trading_fee_discount_futures_percent
        self.trading_fee_discount_margin_percent = trading_fee_discount_margin_percent
        self.trading_fee_discount_spot_percent = trading_fee_discount_spot_percent
        self.trading_fee_percent = trading_fee_percent
        self.trading_fee_use_bnb = trading_fee_use_bnb
        self.lock_create_stop_loss_order = threading.Lock()
        self.ubra_user: BinanceRestApiManager = BinanceRestApiManager(self.binance_public_key,
                                                                      self.binance_private_key,
                                                                      exchange=self.exchange)
        if self.exchange == "binance.com-isolated_margin":
            exchange = "binance.com"
        else:
            exchange = self.exchange
        try:
            self.ubwa_pub: BinanceWebSocketApiManager = \
                BinanceWebSocketApiManager(exchange=exchange,
                                           process_stream_data=self.process_price_feed_stream,
                                           output_default="UnicornFy")
            self.ubwa_user: BinanceWebSocketApiManager = \
                BinanceWebSocketApiManager(exchange=self.exchange,
                                           process_stream_data=self.process_userdata_stream,
                                           output_default="UnicornFy")
        except UnknownExchange:
            self.logger.critical("BinanceTrailingStopLossManager() - Please use a valid exchange!")
            exit()
        self.version = "0.1.1"

    def calculate_stop_loss_amount(self,
                                   amount: float) -> Optional[float]:
        """
        Calculate the tradable stop/loss asset amount (= owning and free - trading fee)

        :param amount: The full owning asset amount.
        :type amount: float

        :return: float or None
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.calculate_stop_loss_amount() - Calculation stop/loss "
                          f"amount without trading fee")
        fee = self.trading_fee_percent
        final_fee = 0
        if self.exchange == "binance.com":
            final_fee = fee
        elif self.exchange == "binance.com-futures":
            final_fee = fee
        elif self.exchange == "binance.com-margin":
            final_fee = fee / 100 * (100-self.trading_fee_discount_margin_percent)
        elif self.exchange == "binance.com-isolated_margin":
            final_fee = fee / 100 * (100-self.trading_fee_discount_margin_percent)
        amount_without_fee = amount/100*(100-final_fee)
        return amount_without_fee

    def calculate_stop_loss_price(self,
                                  price: float) -> Optional[float]:
        """
        Calculate the stop/loss price.

        :param price: Base price used for the calculation
        :type price: float

        :return: float or None
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.calculate_stop_loss_price() - Calculation stop/loss price "
                          f"of base price: {price}")
        if "%" in self.stop_loss_limit:
            limit_percent = float(self.stop_loss_limit.rstrip("%"))
            sl_price = float(price/100)*float(100.0-limit_percent)
        else:
            sl_price = price - float(self.stop_loss_limit)
        sl_price = float(self.round_decimals_down(sl_price, self.precision_crypto))
        return sl_price

    def cancel_open_stop_loss_order(self) -> bool:
        """
        Cancel all open stop/loss orders.

        :return: bool
        """
        if self.exchange == "binance.com-isolated_margin":
            open_orders = self.get_open_orders(stop_loss_market=self.stop_loss_market)
            if open_orders:
                for open_order in open_orders:
                    if open_order['type'] == "STOP_LOSS_LIMIT":
                        self.logger.info(f"BinanceTrailingStopLossManager.cancel_open_stop_loss_order() - Cancelling "
                                         f"open STOP_LOSS_LIMIT order (orderID={open_order['orderId']}) "
                                         f"with stop_loss_price={open_order['price']}.")
                        try:
                            canceled_order = self.ubra_user.cancel_margin_order(symbol=self.stop_loss_market,
                                                                                isIsolated="TRUE",
                                                                                orderId=open_order['orderId'])
                        except BinanceAPIException as error_msg:
                            self.logger.error(f"BinanceTrailingStopLossManager.cancel_open_stop_loss_order() - "
                                              f"error_msg: {error_msg}")
                            return False
                        self.logger.info(f"BinanceTrailingStopLossManager.cancel_open_stop_loss_order() - New "
                                         f"order_status of orderID={canceled_order['orderId']} is"
                                         f" {canceled_order['status']}.")
                        return True
            self.logger.info(f"BinanceTrailingStopLossManager.cancel_open_stop_loss_order() - No open order for "
                             f"cancellation found!")
            return False
        else:
            self.logger.critical(f"BinanceTrailingStopLossManager.cancel_open_stop_loss_order() - no valid exchange "
                                 f"provided!")
            return False

    def create_stop_loss_order(self,
                               stop_loss_price: float = None,
                               current_price: float = None) -> bool:
        """
        Create a stop/loss order!

        :param stop_loss_price: Price to set for the SL order.
        :type stop_loss_price: float
        :param current_price: Current price is optional and only used for logging.
        :type current_price: float

        :return: bool
        """
        with self.lock_create_stop_loss_order:
            if stop_loss_price > self.stop_loss_price:
                self.set_stop_loss_price(stop_loss_price)
            else:
                stop_loss_price = self.stop_loss_price
            if self.cancel_open_stop_loss_order():
                return True
            total, free = self.update_stop_loss_asset_amount()
            if self.keep_threshold is not None:
                stop_loss_quantity = self.round_decimals_down(self.update_stop_loss_quantity(total=total,
                                                                                             free=free),
                                                              self.precision_crypto)
            else:
                stop_loss_quantity = self.calculate_stop_loss_amount(free)

            free = free - stop_loss_quantity
            self.stop_loss_asset_amount_free = free

            if current_price is not None:
                current_price_str = f"current_price={current_price}, "
            else:
                current_price_str = ""
            self.logger.info(f"BinanceTrailingStopLossManager.create_stop_loss_order() - Creating stop/loss "
                             f"order: {current_price_str}"
                             f"stop_price={self.get_stop_loss_trigger_price(stop_loss_price)}, "
                             f"sell_price={stop_loss_price}, "
                             f"owning_amount={total}, "
                             f"owning_amount_free={free}, "
                             f"stop_loss_quantity={stop_loss_quantity} ...")
            if stop_loss_quantity == 0:
                msg = f"Empty stop_loss_quantity in create_stop_loss_order()"
                self.logger.error(f"BinanceTrailingStopLossManager.create_stop_loss_order() - {msg}")
                self.send_email_notificaton(msg)
                self.send_telegram_notification(msg)
                self.stop()
                if self.callback_error is not None:
                    self.callback_error(msg)
                return False
            try:
                new_order = self.ubra_user.create_margin_order(symbol=self.stop_loss_market,
                                                               isIsolated="TRUE",
                                                               side="SELL",
                                                               type="STOP_LOSS_LIMIT",
                                                               price=self.stop_loss_price,
                                                               stopPrice=self.get_stop_loss_trigger_price(stop_loss_price),
                                                               quantity=stop_loss_quantity,
                                                               timeInForce="GTC")
                self.stop_loss_order_id = new_order['orderId']
                self.logger.info(f"BinanceTrailingStopLossManager.create_stop_loss_order() - Created stop/loss order "
                                 f"for market symbol {new_order['symbol']} with orderId="
                                 f"{new_order['orderId']} and side={new_order['side']}.")
            except BinanceAPIException as error_msg:
                self.logger.error(f"BinanceTrailingStopLossManager.create_stop_loss_order() - {error_msg}")
                return False
            return True

    def is_update_available(self) -> bool:
        """
        Is a new release of this package available?
        :return: bool
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.is_update_available() - Starting the request")
        installed_version = self.get_version()
        if ".dev" in installed_version:
            installed_version = installed_version[:-4]
        if self.get_latest_version() == installed_version:
            return False
        elif self.get_latest_version() == "unknown":
            return False
        else:
            return True

    def get_exchange_info(self) -> [dict]:
        """
        Get the exchange info.

        :return: dict or bool
        """
        self.exchange_info = self.ubra_user.get_exchange_info()
        for item in self.exchange_info['symbols']:
            if item['symbol'] == self.stop_loss_market:
                return item
        return False

    def get_open_orders(self,
                        stop_loss_market: str = None) -> Optional[dict]:
        """
        Get the owning amount of the stop/loss asset.

        :return: dict or None
        """
        try:
            if self.exchange == "binance.com":
                open_orders = self.ubra_user.get_open_orders(symbol=stop_loss_market)
                return None
            elif self.exchange == "binance.com-futures":
                open_orders = self.ubra_user.get_open_margin_orders(symbol=stop_loss_market)
                return None
            elif self.exchange == "binance.com-margin":
                open_orders = self.ubra_user.get_open_margin_orders(symbol=stop_loss_market)
                return None
            elif self.exchange == "binance.com-isolated_margin":
                open_orders = self.ubra_user.get_open_margin_orders(symbol=stop_loss_market, isIsolated="True")
            else:
                return None
            return open_orders
        except BinanceAPIException as error_msg:
            self.logger.error(f"BinanceTrailingStopLossManager.get_open_orders() - {error_msg}")
            return None

    def get_owning_amount(self,
                          base_asset: str = None) -> Optional[tuple]:
        """
        Get the owning amount of the stop/loss asset.

        :return: tuple (total, free) or None
        """
        try:
            if self.exchange == "binance.com":
                return None
            elif self.exchange == "binance.com-futures":
                return None
            elif self.exchange == "binance.com-margin":
                return None
            elif self.exchange == "binance.com-isolated_margin":
                account_info = self.ubra_user.get_isolated_margin_account()
                for item in account_info['assets']:
                    base_asset_pool = item['baseAsset']
                    if base_asset_pool['asset'] == base_asset:
                        self.logger.info(f"BinanceTrailingStopLossManager.get_owning_amount() - Owning "
                                         f"{base_asset_pool['asset']}: free={base_asset_pool['free']}, "
                                         f"total={base_asset_pool['totalAsset']} "
                                         f"(interest={base_asset_pool['interest']})")
                        return float(base_asset_pool['totalAsset']), float(base_asset_pool['free'])
                    return None
            else:
                return None
        except BinanceAPIException as error_msg:
            self.logger.error(f"BinanceTrailingStopLossManager.get_owning_amount() - {error_msg}")
            return None

    def get_stop_loss_asset_amount(self) -> Optional[float]:
        """
        Get the current stop/loss asset amount.

        :return: float
        """
        return self.round_decimals_down(self.stop_loss_asset_amount, self.precision_crypto)

    def get_stop_loss_asset_amount_free(self) -> Optional[float]:
        """
        Get the free current stop/loss asset amount.

        :return: float
        """
        return self.round_decimals_down(self.stop_loss_asset_amount_free, self.precision_crypto)

    def get_stop_loss_price(self) -> Optional[float]:
        """
        Get the current stop loss price.

        :return: float
        """
        if self.symbol_info['quote'] == "USDT":
            return self.round_decimals_down(self.stop_loss_price, 2)
        else:
            return self.stop_loss_price

    def get_stop_loss_trigger_price(self,
                                    stop_loss_price: float = 0.0) -> Optional[float]:
        """
        Get the current stop/loss trigger price - if this price gets touched the limit order will get placed in the
        orderbook.

        :return: float
        """
        if "%" in self.stop_loss_trigger_gap:
            gap_percent = float(self.stop_loss_trigger_gap.rstrip("%"))
            trigger_gap = float(self.get_stop_loss_price()/100)*float(100.0-gap_percent)
        else:
            trigger_gap = float(self.stop_loss_trigger_gap)
        trigger_gap = float(self.round_decimals_down(trigger_gap, self.precision_crypto))
        if self.symbol_info['quote'] == "USDT":
            precision = self.precision_fiat
        else:
            precision = self.precision_crypto

        if stop_loss_price == 0:
            stop_loss_price = self.stop_loss_price
        trigger_price = round(stop_loss_price + trigger_gap, 2)
        if len(str(trigger_price).split(".")[1]) <= precision:
            return trigger_price
        else:
            return self.round_decimals_down(trigger_price, precision)

    def get_symbol_info(self,
                        symbol: str = None) -> Optional[dict]:
        """
         Get the symbol info of the stop/loss asset.

         :return: dict
         """
        try:
            if self.exchange == "binance.com":
                return None
            elif self.exchange == "binance.com-futures":
                return None
            elif self.exchange == "binance.com-margin":
                return None
            elif self.exchange == "binance.com-isolated_margin":
                symbol_info = self.ubra_user.get_isolated_margin_symbol(symbol=symbol)
            else:
                symbol_info = None
            return symbol_info
        except BinanceAPIException as error_msg:
            self.logger.error(f"BinanceTrailingStopLossManager.get_symbol_info() - {error_msg}")
            if "APIError(code=-2008): Invalid Api-Key ID" in error_msg:
                exit(1)
            return None

    def get_version(self) -> str:
        """
        Get the package/module version
        :return: str
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.get_version() - Returning the version")
        return self.version

    def process_userdata_stream(self,
                                stream_data: dict = None,
                                stream_buffer_name=False):
        """
        Process the received data of the userData stream.

        :return: bool
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.process_userdata_stream(stream_data={stream_data}, "
                          f"stream_buffer_name={stream_buffer_name}) started ...")
        if stream_data['event_type'] == "executionReport":
            if stream_data['order_id'] == self.stop_loss_order_id:
                if stream_data['current_order_status'] == "FILLED":
                    msg = f"Subject: Stop/Loss Bot '{self.stop_loss_market}'\n\n" \
                          f"STOP LOSS FILLED at price {stream_data['order_price']} (order_id={stream_data['order_id']})"
                    msg_short = f"STOP LOSS FILLED at price {stream_data['order_price']} " \
                                f"(order_id={stream_data['order_id']})"
                    log_msg_short = " ".join(msg_short.strip())
                    self.logger.info(f"BinanceTrailingStopLossManager.get_owning_amount() - {log_msg_short}")
                    self.send_telegram_notification(msg)
                    self.send_email_notificaton(msg)
                    self.stop()
                    if self.callback_finished is not None:
                        self.callback_finished(msg_short)
                    for thread in threading.enumerate():
                        print(f"Thread: {thread.name}")
                    return True
                elif stream_data['current_order_status'] == "CANCELED":
                    self.logger.info(f"BinanceTrailingStopLossManager.process_userdata_stream() - "
                                     f"Received CANCELED event, trigger creation of new order ...")
                    self.create_stop_loss_order(self.stop_loss_price, current_price=self.current_price)
                    return False
            else:
                self.logger.debug(f"BinanceTrailingStopLossManager.process_userdata_stream() - "
                                  f"Received stream_data: {stream_data}")
        elif stream_data['event_type'] == "outboundAccountPosition":
            self.logger.debug(f"BinanceTrailingStopLossManager.process_userdata_stream() - Received: {stream_data}")

    def process_price_feed_stream(self,
                                  stream_data: dict = None,
                                  stream_buffer_name=False) -> bool:
        """
        Process the price feed data:
        Control current price and update `stop_loss_price` or trigger stop/loss if needed.

        :return: bool
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.process_price_feed_stream(stream_data={stream_data}, "
                          f"stream_buffer_name={stream_buffer_name}) started ...")
        if stream_data.get('price'):
            self.current_price = stream_data.get('price')
            sl_price = self.calculate_stop_loss_price(float(stream_data.get('price')))
            if self.stop_loss_price is None:
                self.logger.info(f"BinanceTrailingStopLossManager.process_price_feed_stream() - Setting "
                                 f"stop_loss_price from None to {sl_price}!")
                self.create_stop_loss_order(sl_price, current_price=stream_data.get('price'))
            elif self.stop_loss_price < sl_price:
                self.logger.info(f"BinanceTrailingStopLossManager.process_price_feed_stream() - Setting "
                                 f"stop_loss_price from {self.stop_loss_price} to {sl_price}!")
                self.create_stop_loss_order(sl_price, current_price=stream_data.get('price'))
        return True

    @staticmethod
    def round_decimals_down(number: float,
                            decimals: int = 2) -> float:
        """
        Returns a value rounded down to a specific number of decimal places.
        :param number: The decimal number to round down.
        :type number: float
        :param decimals: How many decimals you want to keep.
        :type decimals: int
        :return: float
        """
        if not isinstance(decimals, int):
            raise TypeError("BinanceTrailingStopLossManager.round_decimals_down() - Decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("BinanceTrailingStopLossManager.round_decimals_down() - Decimal places has to be 0 or "
                             "more")
        elif decimals == 0:
            return math.floor(number)
        else:
            factor = 10 ** decimals
            return math.floor(number * factor) / factor

    def send_email_notificaton(self,
                               message: str = None) -> bool:
        """
        Send a notification via email!

        :param message: Text to send via email.
        :type message: str

        :return:
        """
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.send_from_email_server, self.send_from_email_port, context=context) as server:
            server.login(self.send_from_email_address, self.send_from_email_password)
            server.sendmail(self.send_from_email_address, self.send_to_email_address, message)
            self.logger.info(f"BinanceTrailingStopLossManager.send_email_notificaton() - Email sent!")
            return True

    def send_telegram_notification(self,
                                   message: str = None) -> bool:
        """
        Send a notification via telegram!

        :param message: Text to send via Telegram.
        :type message: str

        :return:
        """
        date = datetime.datetime.now().strftime("%H:%M:%S")
        msg = message.replace("%25", "%")
        logging.info(" ".join([msg, "at", date]))
        request_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage?chat_id=" \
                      f"{self.telegram_send_to}&parse_mode=HTML&text={message}"
        response = requests.get(request_url)
        self.logger.info(f"BinanceTrailingStopLossManager.send_telegram_message() - response: {response}")
        return True

    def start(self) -> bool:
        """
        Start Stop/Loss with provided settings!

        :return: bool
        """
        self.logger.info(f"BinanceTrailingStopLossManager.start() - Starting trailing stop/loss on {self.exchange} "
                         f"for the market {self.stop_loss_market} ...")
        self.logger.debug(f"BinanceTrailingStopLossManager.start() - reset_stop_loss_price={self.reset_stop_loss_price}")
        self.symbol_info = self.get_symbol_info(symbol=self.stop_loss_market)
        self.logger.info(f"BinanceTrailingStopLossManager.start() -  used_weight: {self.ubra_user.get_used_weight()}")
        self.stop_loss_asset_name = self.symbol_info['base']
        self.exchange_info = self.get_exchange_info()
        self.update_stop_loss_asset_amount()

        if self.exchange == "binance.com-isolated_margin":
            symbol = self.stop_loss_market
        else:
            symbol = False
        user_stream_id = self.ubwa_user.create_stream("arr", "!userData",
                                                      api_key=self.binance_public_key,
                                                      api_secret=self.binance_private_key,
                                                      symbols=symbol,
                                                      stream_label="UserData")
        self.ubwa_pub.create_stream(channels="aggTrade",
                                    markets=self.stop_loss_market,
                                    stream_label="PriceFeed")

        self.logger.info(f"BinanceTrailingStopLossManager.start() - Waiting till userData stream is running ...")
        if self.ubwa_user.wait_till_stream_has_started(user_stream_id):
            time.sleep(5)
            self.logger.info(f"BinanceTrailingStopLossManager.start() - User stream is running!")

        if self.stop_loss_price is None or self.stop_loss_price == 0.0:
            if self.reset_stop_loss_price is not True:
                open_orders = self.get_open_orders(stop_loss_market=self.stop_loss_market)
                if open_orders:
                    for open_order in open_orders:
                        if open_order['type'] == "STOP_LOSS_LIMIT":
                            self.logger.info(f"BinanceTrailingStopLossManager.start() - Found open STOP_LOSS_LIMIT "
                                             f"order with stop_loss_price={open_order['price']}.")
                            self.create_stop_loss_order(float(open_order['price']))
                else:
                    self.logger.info(f"BinanceTrailingStopLossManager.start() - No open STOP_LOSS_LIMIT orders found!")
            else:
                self.logger.info(f"BinanceTrailingStopLossManager.start() - Resetting old stop_loss_price!")
        else:
            self.logger.info(f"BinanceTrailingStopLossManager.start() - Using provided stop_loss_price="
                             f"{self.stop_loss_price}")
            self.create_stop_loss_order(self.stop_loss_price)
        return True

    def stop(self) -> bool:
        """
        Stop stop_loss! :)

        :return: bool
        """
        self.logger.info(f"BinanceTrailingStopLossManager.stop() - Gracefully stopping unicorn-binance-stop-loss "
                         f"engine ...")
        self.stop_request = True
        try:
            self.ubwa_pub.stop_manager_with_all_streams()
            self.ubwa_user.stop_manager_with_all_streams()
            return True
        except KeyboardInterrupt:
            print("\nStopping ... just wait a few seconds!")
        try:
            self.ubwa_user.stop_manager_with_all_streams()
            return True
        except KeyboardInterrupt:
            print("\nStopping ... just wait a few seconds!")

    def set_stop_loss_price(self,
                            stop_loss_price: float = None) -> bool:
        """
        Set the stop/loss price.

        :param stop_loss_price: Price to set for the SL order.
        :type stop_loss_price: float

        :return: bool
        """
        self.logger.debug(f"BinanceTrailingStopLossManager.set_stop_loss_price() - Setting new stop_loss_price={stop_loss_price} ...")
        self.stop_loss_price = stop_loss_price
        return True

    def update_stop_loss_quantity(self,
                                  total: float = 0.0,
                                  free: float = 0.0) -> float:
        """
        Calculate and update the stop_loss_quantity!

        :param total: Total asset amount
        :type total: float
        :param free: Free asset amount
        :type free: float

        :return: float
        """
        self.logger.info(f"BinanceTrailingStopLossManager.update_stop_loss_quantity() - Calculating the "
                         f"stop_loss_quantity amount.")
        if "%" in self.keep_threshold:
            keep_threshold_percent = float(self.keep_threshold.rstrip("%"))
            keep_threshold_float = total/100*keep_threshold_percent
        else:
            keep_threshold_float = float(self.keep_threshold)
        if keep_threshold_float > free:
            msg = f"BinanceTrailingStopLossManager.update_stop_loss_quantity() - Nothing to do - `keep_threshold` " \
                  f"is greater then `stop_loss_asset_amount_free`!"
            self.logger.critical(msg)
            self.send_telegram_notification(msg)
            self.send_email_notificaton(msg)
            self.stop()
            if self.callback_error is not None:
                self.callback_error(msg)
            return False
        stop_loss_quantity = free - keep_threshold_float
        self.stop_loss_quantity = stop_loss_quantity
        return stop_loss_quantity

    def update_stop_loss_asset_amount(self,
                                      total: float = None,
                                      free: float = None) -> tuple:
        """
        Update the owning asset amount (total, free)!

        :param total: Total amount of the stop_loss_asset!
        :type total: float
        :param free: Free amount of the stop_loss_asset!
        :type free: float

        :return: tuple
        """
        if total is None or free is None:
            total, free = self.get_owning_amount(base_asset=self.stop_loss_asset_name)
        self.stop_loss_asset_amount = float(total)
        self.stop_loss_asset_amount_free = float(free)
        return total, free
