#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: manager.py
#
# Part of ‘UNICORN Binance Trailing Stop Loss’
# Project website: https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
# Documentation: https://unicorn-binance-trailing-stop-loss.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-trailing-stop-loss
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
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

from unicorn_binance_trailing_stop_loss.cli import main
from unicorn_binance_trailing_stop_loss.manager import BinanceTrailingStopLossManager
import logging
import unittest
import os

BINANCE_COM_API_KEY = ""
BINANCE_COM_API_SECRET = ""

logging.getLogger("unicorn_binance_trailing_stop_loss.unicorn_binance_trailing_stop_loss_engine_manager")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

print(f"Starting unittests:")


def callback_error(msg):
    print(f"STOP LOSS ERROR - ENGINE IS SHUTTING DOWN! - {msg}")
    UBTSL.stop_manager()


def callback_finished(msg):
    print(f"STOP LOSS FINISHED - ENGINE IS SHUTTING DOWN! - {msg}")
    UBTSL.stop_manager()


UBTSL = BinanceTrailingStopLossManager(callback_error=callback_error,
                                       callback_finished=callback_finished,
                                       binance_public_key="aaa",
                                       binance_private_key="bbb",
                                       exchange="binance.com-testnet",
                                       keep_threshold="20%",
                                       reset_stop_loss_price=True,
                                       send_to_email_address="blah@example.com",
                                       send_from_email_address="blub@example.com",
                                       send_from_email_password="pass",
                                       send_from_email_server="mail.example.com",
                                       send_from_email_port=25,
                                       stop_loss_limit="1.5%",
                                       market="LUNAUSDT",
                                       stop_loss_order_type="LIMIT",
                                       stop_loss_price=88,
                                       telegram_bot_token="telegram_bot_token",
                                       telegram_send_to="telegram_send_to")

print("Testing: ")


class TestBinanceComManager(unittest.TestCase):
    def test_stop(self):
        self.assertTrue(UBTSL.stop_manager())

    def test_cli(self):
        try:
            main()
        except SystemExit:
            pass

    def test_notification(self):
        BinanceTrailingStopLossManager(callback_error=callback_error,
                                       callback_finished=callback_finished,
                                       binance_public_key="aaa",
                                       binance_private_key="bbb",
                                       exchange="binance.com-testnet",
                                       keep_threshold="20%",
                                       reset_stop_loss_price=True,
                                       send_to_email_address="blah@example.com",
                                       send_from_email_address="blub@example.com",
                                       send_from_email_password="pass",
                                       send_from_email_server="mail.example.com",
                                       send_from_email_port=25,
                                       stop_loss_limit="1.5%",
                                       market="LUNAUSDT",
                                       stop_loss_order_type="LIMIT",
                                       stop_loss_price=88,
                                       telegram_bot_token="telegram_bot_token",
                                       telegram_send_to="telegram_send_to",
                                       test="notification")

    def test_binance_connectivity(self):
        BinanceTrailingStopLossManager(callback_error=callback_error,
                                       callback_finished=callback_finished,
                                       binance_public_key="aaa",
                                       binance_private_key="bbb",
                                       exchange="binance.com-testnet",
                                       keep_threshold="20%",
                                       reset_stop_loss_price=True,
                                       send_to_email_address="blah@example.com",
                                       send_from_email_address="blub@example.com",
                                       send_from_email_password="pass",
                                       send_from_email_server="mail.example.com",
                                       send_from_email_port=25,
                                       stop_loss_limit="1.5%",
                                       market="LUNAUSDT",
                                       stop_loss_order_type="LIMIT",
                                       stop_loss_price=88,
                                       telegram_bot_token="telegram_bot_token",
                                       telegram_send_to="telegram_send_to",
                                       test="binance-connectivity")

    def test_streams(self):
        BinanceTrailingStopLossManager(callback_error=callback_error,
                                       callback_finished=callback_finished,
                                       binance_public_key="aaa",
                                       binance_private_key="bbb",
                                       exchange="binance.com-testnet",
                                       keep_threshold="20%",
                                       reset_stop_loss_price=True,
                                       send_to_email_address="blah@example.com",
                                       send_from_email_address="blub@example.com",
                                       send_from_email_password="pass",
                                       send_from_email_server="mail.example.com",
                                       send_from_email_port=25,
                                       stop_loss_limit="1.5%",
                                       market="LUNAUSDT",
                                       stop_loss_order_type="LIMIT",
                                       stop_loss_price=88,
                                       telegram_bot_token="telegram_bot_token",
                                       telegram_send_to="telegram_send_to",
                                       test="streams20")


if __name__ == '__main__':
    unittest.main()
