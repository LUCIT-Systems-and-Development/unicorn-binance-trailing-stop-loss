#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unicorn_binance_trailing_stop_loss/bot.py
#
# Part of ‘UNICORN Binance Trailing Stop Loss’
# Project website: https://github.com/LUCIT-Systems-and-Development/lucit_general_toolset
# Documentation: https://lucit-systems-and-development.github.io/lucit_general_toolset
# PyPI: https://pypi.org/project/lucit_general_toolset
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

from manager import BinanceTrailingStopLossManager
from configparser import ConfigParser, ExtendedInterpolation

import argparse
import logging
import os
import sys
import time

# Set specific logger
logger = logging.getLogger("unicorn_binance_trailing_stop_loss_bot")
logger.setLevel(logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('--apikey',
                    type=str,
                    help="The API key!",
                    required=False)
parser.add_argument('--apisecret',
                    type=str,
                    help="The API secret!",
                    required=False)
parser.add_argument('--exchange',
                    type=str,
                    help="Exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...",
                    required=False)
parser.add_argument('--keepthreshold',
                    type=str,
                    help="Exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...",
                    required=False)
parser.add_argument('--limit',
                    type=str,
                    help='Stop/loss limit in integer or percent.',
                    required=False)
parser.add_argument('--logfile',
                    type=str,
                    help='Specify path including filename to the logfile.',
                    required=False)
parser.add_argument('--orderside',
                    type=str,
                    help="Specify whether the trailing stop loss should be in buying or selling mode. (Ex: 'buy' "
                         "or 'sell').",
                    required=False)
parser.add_argument('--ordertype',
                    type=str,
                    help="Use `limit` or `market`.",
                    required=False)
parser.add_argument('--profile',
                    type=str,
                    help='Name of the profile to load from profiles.ini!',
                    required=False)
parser.add_argument('--resetstoplossprice',
                    type=str,
                    help='Reset the existing stop_loss_price! Usage: True anything else is False!',
                    required=False)
parser.add_argument('--secrets',
                    type=str,
                    help='Specify path including filename to the secrets file. (Ex: `~/secrets.ini`) If not '
                         'available it tries to load a secrets.ini from the current working directory.',
                    required=False)
parser.add_argument('--stoplossprice',
                    type=float,
                    help='Set the starting stop/loss price.',
                    required=False)
parser.add_argument('--symbol',
                    type=str,
                    help='The market symbol as used by Binance.',
                    required=False)
options = parser.parse_args()


def callback_error(msg):
    print(f"STOP LOSS ERROR - ENGINE IS SHUTTING DOWN! - {msg}")


def callback_finished(msg):
    print(f"STOP LOSS FINISHED - ENGINE IS SHUTTING DOWN! - {msg}")


if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if options.logfile is True:
    logfile = options.logfile
else:
    logfile = os.path.basename(__file__) + '.log'
# Todo: Use the Logfile name :)

# Load secrets.ini file
if options.secrets is not None:
    # Load from cli arg if provided
    config_file = str(options.secrets)
else:
    # Load secrets from default filename
    config_file = "secrets.ini2"
    if os.path.isfile(config_file) is False:
        logger.critical("If secrets.ini is not in the same directory or is renamed, then the parameter --secrets "
                        "is mandatory! Please use --help for further information!")
        sys.exit(1)
logging.info(f"Loading configuration file {config_file}")
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

# Load profiles
profiles_file = "../profiles.ini"
logging.info(f"Loading profiles file {profiles_file}")
profiles = ConfigParser(interpolation=ExtendedInterpolation())
profiles.read(profiles_file)

exchange = ""
keep_threshold = ""
stop_loss_market = ""
stop_loss_limit = ""
stop_loss_order_type = ""
stop_loss_price: float = 0.0
stop_loss_side = ""
reset_stop_loss_price: bool = False

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
        stop_loss_market = profiles[options.profile]['stop_loss_market']
    except KeyError:
        pass
    try:
        stop_loss_limit = profiles[options.profile]['stop_loss_limit']
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
if options.exchange is not None:
    exchange = options.exchange
if options.keepthreshold is not None:
    keep_threshold = options.keepthreshold
if options.symbol is not None:
    stop_loss_market = options.symbol
if options.limit is not None:
    stop_loss_limit = options.limit
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

ubtsl = BinanceTrailingStopLossManager(callback_error=callback_error,
                                       callback_finished=callback_finished,
                                       binance_public_key=public_key,
                                       binance_private_key=private_key,
                                       exchange=exchange,
                                       keep_threshold=keep_threshold,
                                       reset_stop_loss_price=reset_stop_loss_price,
                                       send_to_email_address=send_to_email_address,
                                       send_from_email_address=send_from_email_address,
                                       send_from_email_password=send_from_email_password,
                                       send_from_email_server=send_from_email_server,
                                       send_from_email_port=send_from_email_port,
                                       stop_loss_limit=stop_loss_limit,
                                       stop_loss_market=stop_loss_market,
                                       stop_loss_order_type=stop_loss_order_type,
                                       stop_loss_price=stop_loss_price,
                                       stop_loss_side=stop_loss_side,
                                       telegram_bot_token=telegram_bot_token,
                                       telegram_send_to=telegram_send_to)
ubtsl.start()

try:
    while ubtsl.stop_request is False:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping ... just wait a few seconds!")
    ubtsl.stop()
print(f"Exit main file!")
