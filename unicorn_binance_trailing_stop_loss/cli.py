#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unicorn_binance_trailing_stop_loss/cli.py
#
# Part of ‘UNICORN Binance Trailing Stop Loss’
# Project website: https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
# Documentation: https://unicorn-binance-trailing-stop-loss.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-trailing-stop-loss
#
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

from unicorn_binance_trailing_stop_loss.manager import BinanceTrailingStopLossManager
from unicorn_binance_rest_api.manager import BinanceRestApiManager, BinanceAPIException
from configparser import ConfigParser, ExtendedInterpolation
import argparse
import logging
import platform
import os
import sys
import textwrap
import time
from pathlib import Path

"""
    UNICORN Binance Trailing Stop Loss Command Line Interface Documentation
"""


def main():
    version = BinanceTrailingStopLossManager.get_version()
    os_type = platform.system()
    if os_type == "Windows":
        path_separator = "\\"
    else:
        path_separator = "/"
    home_path = str(Path.home()) + path_separator
    log_format = "{asctime} [{levelname:8}] {process} {thread} {module}: {message}"

    parser = argparse.ArgumentParser(
          description=f"UNICORN Binance Trailing Stop Loss {version} (MIT License)",
          prog=f"ubtsl",
          formatter_class=argparse.RawDescriptionHelpFormatter,
          epilog=textwrap.dedent('''\
             examples:
                 Check if a new update is available:
                 $ ubtsl --checkupdate

                 Show program version:
                 $ ubtsl --version
                 
                 Test notifications:
                 $ ubtsl --test notification
                 
                 Start with profile "LUNAUSDT_SELL" and overwrite the stoplosslimit:
                 $ ubtsl --profile LUNAUSDT_SELL --stoplosslimit 0.5%
                 
             additional information:
                 Author: https://www.lucit.tech
                 Changes: https://unicorn-binance-trailing-stop-loss.docs.lucit.tech//CHANGELOG.html
                 Documentation: https://lucit-systems-and-development.github.io/unicorn-binance-trailing-stop-loss
                 Issue Tracker: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues
                 Source: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
                 Wiki: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/wiki
                 
             disclaimer:
                 This project is for informational purposes only. You should not construe this information or any other material as 
                 legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
                 endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
                 this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
                 jurisdiction.
                
                 If you intend to use real money, use it at your own risk.
                
                 Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
                 of any kind, including but not limited to direct or indirect damages for loss of profits.
             '''))

    parser.add_argument('-ak', '--apikey',
                        type=str,
                        help="the API key",
                        required=False)
    parser.add_argument('-as', '--apisecret',
                        type=str,
                        help="the API secret",
                        required=False)
    parser.add_argument('-cf', '--configfile',
                        type=str,
                        help='specify path including filename to the config file (ex: `~/my_config.ini`). if not '
                             'provided ubtsl tries to load a `ubtsl_config.ini` from the home and the current working '
                             'directory.',
                        required=False)
    parser.add_argument('-cu', '--checkupdate',
                        help=f'check if update is available',
                        required=False,
                        action='store_true')
    parser.add_argument('-e', '--exchange',
                        type=str,
                        help="exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...",
                        required=False)
    parser.add_argument('-n', '--engine',
                        type=str,
                        help='default: `trail`, options: `jump-in-and-trail` to place a market buy order and trail',
                        required=False)
    parser.add_argument('-k', '--keepthreshold',
                        type=str,
                        help="exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...",
                        required=False)
    parser.add_argument('-lf', '--logfile',
                        type=str,
                        help='specify path including filename to the logfile',
                        required=False)
    parser.add_argument('-ll', '--loglevel',
                        type=str,
                        help='default: INFO\r\n'
                             'available log levels: DEBUG, INFO, WARNING, ERROR and CRITICAL',
                        required=False)
    parser.add_argument('-os', '--orderside',
                        type=str,
                        help="specify whether the trailing stop loss should be in buying or selling mode. (ex: 'buy' "
                             "or 'sell')",
                        required=False)
    parser.add_argument('-ot', '--ordertype',
                        type=str,
                        help="use `limit` or `market`",
                        required=False)
    parser.add_argument('-pf', '--profile',
                        type=str,
                        help='name of the profile to load from ubtsl_profiles.ini!',
                        required=False)
    parser.add_argument('-pff', '--profilesfile',
                        type=str,
                        help='specify path including filename to the profiles file (ex: `~/my_profiles.ini`). if not '
                             'available ubtsl tries to load a ubtsl_profile.ini from the home and the current working '
                             'directory',
                        required=False)
    parser.add_argument('-r', '--resetstoplossprice',
                        type=str,
                        help='reset the existing stop_loss_price! usage: True anything else is False',
                        required=False)
    parser.add_argument('-l', '--stoplosslimit',
                        type=str,
                        help='stop/loss limit in float or percent',
                        required=False)
    parser.add_argument('-p', '--stoplossprice',
                        type=float,
                        help='set the start stop/loss price as float value',
                        required=False)
    parser.add_argument('-sl', '--stoplossstartlimit',
                        type=str,
                        help='set the start stop/loss limit in float or percent. (only used in `jump-in-and-trail`',
                        required=False)
    parser.add_argument('-s', '--symbol',
                        type=str,
                        help='the market symbol as used by binance',
                        required=False)
    parser.add_argument('-t', '--test',
                        type=str,
                        help='use this to test specific systems like "notification". if test is not None the engine '
                             'will NOT start! it only tests!',
                        required=False)
    parser.add_argument('-v', '--version',
                        help=f'show the program version, which is `{version}` by the way :)',
                        required=False,
                        action='store_true')
    options = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    # Update available?
    if options.checkupdate is True:
        ubtsl = BinanceTrailingStopLossManager(start_engine=False, warn_on_update=False)
        if ubtsl.is_update_available():
            print("A new update is available: https://github.com/LUCIT-Systems-and-Development/"
                  "unicorn-binance-trailing-stop-loss/releases/latest")
        else:
            print("No update found!")
        ubtsl.stop_manager()
        sys.exit(0)

    # Print the version
    if options.version is True:
        print(f"UNICORN Binance Trailing Stop Loss {version}")
        sys.exit(0)

    def callback_error(message):
        print(f"STOP LOSS ERROR - ENGINE IS SHUTTING DOWN! - {message}")
        ubtsl.stop_manager()

    def callback_finished(order):
        if engine == "jump-in-and-trail":
            fee = 0.2
            print(f"======================================================\r\n"
                  f"buy_price: {float(buy_price):g}\r\n"
                  f"sell_price: {float(order['order_price']):g}\r\n"
                  f"fee: ~{fee}%\r\n"
                  f"------------------------------------------------------\r\n"
                  f"profit: {fee*(float(order['order_price'])-float(buy_price))}")
        ubtsl.stop_manager()

    # Log file
    if options.logfile is True:
        logfile = options.logfile
    else:
        logfile = os.path.basename(__file__) + '.log'

    # Log level
    if options.loglevel == "DEBUG":
        loglevel = logging.DEBUG
    elif options.loglevel == "INFO":
        loglevel = logging.INFO
    elif options.loglevel == "WARN" or options.loglevel == "WARNING" :
        loglevel = logging.WARNING
    elif options.loglevel == "ERROR":
        loglevel = logging.ERROR
    elif options.loglevel == "CRITICAL":
        loglevel = logging.CRITICAL
    else:
        loglevel = logging.INFO

    # Config logger
    logging.basicConfig(level=loglevel,
                        filename=logfile,
                        format=log_format,
                        style="{")
    logger = logging.getLogger("unicorn_binance_trailing_stop_loss")
    logger.info(f"Started ubtsl_{version}")
    print(f"Started ubtsl_{version}")

    test = None
    if options.test is not None:
        test = options.test

    # Load config.ini file
    if options.configfile is not None:
        # Load from cli arg if provided
        config_file = str(options.configfile)
    else:
        # Load secrets from default filenames
        config_file_lucit = f"{home_path}.lucit/trading_tools.ini"
        config_file_cwd = f"ubtsl_config.ini"
        config_file_home = f"{home_path}.lucit/ubtsl_config.ini"
        if os.path.isfile(config_file_lucit):
            config_file = config_file_lucit
        elif os.path.isfile(config_file_cwd):
            config_file = config_file_cwd
        elif os.path.isfile(config_file_home):
            config_file = config_file_home
        else:
            logger.critical(f"If ´ubtsl_secrets.ini´ is not in the `{home_path}lucit` or current working directory or "
                            f"is renamed, then the parameter --secretsfile is mandatory! Please use --help for "
                            f"further information!")
            print(f"If ´ubtsl_secrets.ini´ is not in the `{home_path}lucit` or current working directory or is renamed"
                  f", then the parameter --secretsfile is mandatory! Please use --help for further information!")
            sys.exit(1)

    logger.info(f"Loading configuration file `{config_file}`")
    print(f"Loading configuration file `{config_file}`")

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(config_file)
    public_key = config['BINANCE']['api_key']
    private_key = config['BINANCE']['api_secret']
    send_to_email_address = config['EMAIL']['send_to_email']
    send_from_email_address = config['EMAIL']['send_from_email']
    send_from_email_password = config['EMAIL']['send_from_password']
    send_from_email_server = config['EMAIL']['send_from_server']
    send_from_email_port = config['EMAIL']['send_from_port']
    telegram_bot_token = config['TELEGRAM']['bot_token']
    telegram_send_to = config['TELEGRAM']['send_to']

    # Load profiles.ini file
    if options.profilesfile is not None:
        # Load from cli arg if provided
        profiles_file = str(options.profilesfile)
    else:
        profiles_file_cwd = "ubtsl_profiles.ini"
        profiles_file_home = f"{home_path}.lucit/ubtsl_profiles.ini"
        if os.path.isfile(profiles_file_cwd):
            profiles_file = profiles_file_cwd
        elif os.path.isfile(profiles_file_home):
            profiles_file = profiles_file_home
        else:
            if test is None:
                logger.critical("If ´ubtsl_profiles.ini´ is not in the home or current working directory or is renamed, "
                                "then the parameter --profilesfile is mandatory! Please use --help for further "
                                "information!")
                print("If ´ubtsl_profiles.ini´ is not in the home or current working directory or is renamed, then "
                      "the parameter --profilesfile is mandatory! Please use --help for further information!")
                sys.exit(1)

    logger.info(f"Loading profiles file `{profiles_file}`")
    print(f"Loading profiles file `{profiles_file}`")
    profiles = ConfigParser(interpolation=ExtendedInterpolation())
    profiles.read(profiles_file)

    engine = "trail"
    exchange = ""
    keep_threshold = ""
    stop_loss_market = ""
    stop_loss_limit = ""
    stop_loss_start_limit = ""
    stop_loss_order_type = ""
    stop_loss_price: float = 0.0
    stop_loss_side = ""
    reset_stop_loss_price = False

    # Load a profile is provided via argparse
    if options.profile is not None:
        try:
            exchange = profiles[options.profile]['exchange']
        except KeyError:
            pass
        try:
            keep_threshold = profiles[options.profile]['keep_threshold']
        except KeyError:
            pass
        try:
            reset_stop_loss_price = profiles[options.profile]['reset_stop_loss_price']
        except KeyError:
            pass
        try:
            engine = profiles[options.profile]['engine']
        except KeyError:
            pass
        try:
            stop_loss_market = profiles[options.profile]['stop_loss_market']
        except KeyError:
            pass
        try:
            stop_loss_limit = profiles[options.profile]['stop_loss_limit']
        except KeyError:
            pass
        try:
            stop_loss_start_limit = profiles[options.profile]['stop_loss_start_limit']
        except KeyError:
            pass
        try:
            stop_loss_order_type = profiles[options.profile]['stop_loss_order_type']
        except KeyError:
            pass
        try:
            stop_loss_price = float(profiles[options.profile]['stop_loss_price'])
        except KeyError:
            pass
        try:
            stop_loss_side = profiles[options.profile]['stop_loss_side']
        except KeyError:
            pass

    # cli args overwrite profile settings
    if options.apikey is not None:
        public_key = options.apikey
    if options.apisecret is not None:
        private_key = options.apisecret
    if options.engine is not None:
        engine = options.engine
    if options.exchange is not None:
        exchange = options.exchange
    if options.keepthreshold is not None:
        keep_threshold = options.keepthreshold
    if options.symbol is not None:
        stop_loss_market = options.symbol
    if options.stoplosslimit is not None:
        stop_loss_limit = options.stoplosslimit
    if options.stoplossstartlimit is not None:
        stop_loss_start_limit = options.stoplossstartlimit
    if options.ordertype is not None:
        stop_loss_order_type = options.ordertype
    if options.resetstoplossprice is not None:
        reset_stop_loss_price = options.resetstoplossprice
    if options.stoplossprice is not None:
        stop_loss_price = options.stoplossprice
    if options.orderside is not None:
        stop_loss_side = options.orderside

    if str(reset_stop_loss_price).upper() == "TRUE":
        reset_stop_loss_price = True
    else:
        reset_stop_loss_price = False

    if test is None:
        if engine == "jump-in-and-trail":
            logger.info(f"Starting jump-in-and-trail engine")
            print(f"Starting jump-in-and-trail engine")
            ubra = BinanceRestApiManager(api_key=public_key, api_secret=private_key, exchange=exchange)
            if exchange == "binance.com-isolated_margin":
                stop_loss_side = "SELL"
                isolated_margin_account = ubra.get_isolated_margin_account()
                if isolated_margin_account['assets'][0]['symbol'] == stop_loss_market:
                    # Todo: Calc borrow_threshold
                    # Todo: Take full loan
                    # ask_price = ubra.get_ticker(symbol=stop_loss_market)['askPrice']
                    free_quote_asset = isolated_margin_account['assets'][0]['quoteAsset']['free']
                    try:
                        margin_order = ubra.create_margin_order(symbol=stop_loss_market,
                                                                isIsolated="TRUE",
                                                                side="BUY",
                                                                type="MARKET",
                                                                quoteOrderQty=free_quote_asset,
                                                                sideEffectType="MARGIN_BUY")
                    except BinanceAPIException as error_msg:
                        msg = f"Stopping because of Binance API exception: {error_msg}"
                        logging.critical(msg)
                        print(msg)
                        sys.exit(1)
                    logger.info(f"Jumped in with buy order: {margin_order}")
                    print(f"Jumped in with buy price: {margin_order['fills'][0]['price']}")

                    # Todo: Use this block as a static method within ubtsl.manager
                    # Todo: Calculate the average price instead of using the price of the first execution:
                    buy_price = margin_order['fills'][0]['price']
                    if "%" in stop_loss_start_limit:
                        limit_percent = float(stop_loss_start_limit.rstrip("%"))
                        sl_price = float(float(margin_order['fills'][0]['price']) / 100) * float(100.0 - limit_percent)
                    else:
                        sl_price = float(margin_order['fills'][0]['price']) - float(stop_loss_start_limit)
                    stop_loss_price = float(BinanceTrailingStopLossManager.round_decimals_down(sl_price, 2))
            else:
                logger.critical(f"Option `jump-in-and-trail` in parameter `engine` is not supported for exchange "
                                f"'{exchange}'.")
                print(f"Option `jump-in-and-trail` in parameter `engine` is not supported for exchange '{exchange}'.")
                sys.exit(1)

    ubtsl = BinanceTrailingStopLossManager(callback_error=callback_error,
                                           callback_finished=callback_finished,
                                           binance_public_key=public_key,
                                           binance_private_key=private_key,
                                           exchange=exchange,
                                           keep_threshold=keep_threshold,
                                           print_notificatons=True,
                                           reset_stop_loss_price=reset_stop_loss_price,
                                           send_to_email_address=send_to_email_address,
                                           send_from_email_address=send_from_email_address,
                                           send_from_email_password=send_from_email_password,
                                           send_from_email_server=send_from_email_server,
                                           send_from_email_port=int(send_from_email_port),
                                           stop_loss_limit=stop_loss_limit,
                                           stop_loss_market=stop_loss_market,
                                           stop_loss_order_type=stop_loss_order_type,
                                           stop_loss_price=stop_loss_price,
                                           stop_loss_side=stop_loss_side,
                                           telegram_bot_token=telegram_bot_token,
                                           telegram_send_to=telegram_send_to,
                                           test=test)
    if test is None:
        try:
            while ubtsl.stop_request is False:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping ... just wait a few seconds!")
            ubtsl.stop_manager()


if __name__ == "__main__":
    main()
