[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/releases)
[![Conda Release](https://img.shields.io/conda/vn/conda-forge/unicorn-binance-trailing-stop-loss.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-trailing-stop-loss)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/unicorn-binance-trailing-stop-loss.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-trailing-stop-loss)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-trailing-stop-loss?color=blue)](https://pypi.org/project/unicorn-binance-trailing-stop-loss/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-trailing-stop-loss)](https://pepy.tech/project/unicorn-binance-trailing-stop-loss)
[![License](https://img.shields.io/github/license/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss.svg?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/LICENSE)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_trailing_stop_loss.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_trailing_stop_loss.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/alerts/)
[![Unit Tests](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/actions/workflows/unit-tests.yml)
[![Azure Pipelines](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/unicorn-binance-trailing-stop-loss-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=15698&branchName=main)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/)
[![Github](https://img.shields.io/badge/source-github-yellow)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow)](https://t.me/unicorndevs)
[![Gitter](https://badges.gitter.im/unicorn-binance-suite/unicorn-binance-trailing-stop-loss.svg)](https://gitter.im/unicorn-binance-suite/unicorn-binance-trailing-stop-loss?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# UNICORN Binance Trailing Stop Loss Bot

[Description](#description) | [Installation](#installation) | [Disclaimer](#disclaimer) | [Commercial Support](#commercial-support)

After starting the engine, a stop/loss order is placed and trailed until it is completely fulfilled. If desired, a 
notification can be sent via email and Telegram afterwards.

In addition, there is a smart entry option called `jump-in-and-trail`. This offers the possibility to buy spot, future 
and margin assets with a limit or market order and then to trail a stop/loss order until sold.

The `UNICORN Binance Trailing Stop Loss Bot` uses the engine of the Python library [`unicorn-binance-trailing-stop-loss`](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html) 
and has the exact same interface and configuration setup as the[`UNICORN Binance Trailing Stop Loss CLI`](https://www.lucit.tech/ubtsl-cli.html). 

The bot only does not require a pre-installed Python environment and can be easily installed on [Windows](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html#windows) 
and [Mac](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html#mac) with a 
setup file. If you already have an installed Python environment, we recommend [installing via PIP](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html#installation-and-upgrade) 
and using the [`UNICORN Binance Trailing Stop Loss CLI`](https://www.lucit.tech/ubtsl-cli.html).

Please read carefully all provided [documentation](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/) and 
look in the [issues](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues) about 
known problems before using this tool - you use it at your own risk!

If you put this bot on a market, you should stop trading manually on this market yourself!

For more information about the usage [read here](https://www.lucit.tech/ubtsl-cli.html).

## Description
The Bot and [CLI version](https://www.lucit.tech/ubtsl-cli.html) are absolutely identical, except for the installation 
method and that the Bot version does not require a pre-installed Python environment. Please read the 
[CLI description](https://www.lucit.tech/ubtsl-cli.html#description) for more information. 

## Installation
### Windows
Download [ubtsl_setup.exe](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/releases/latest)
from GitHub.

### Mac
Comming soon!

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

***If you intend to use real money, use it at your own risk.***

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.

## Commercial Support
[![LUCIT](https://www.lucit.tech/files/images/logos/LUCIT-LOGO.png)](https://www.lucit.tech)

***Do you need a developer, operator or consultant?***

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding initial consultation via my company 
[LUCIT](https://www.lucit.tech) from Vienna (Austria) or via [Telegram](https://t.me/LUCIT_OZ)/[WhatsApp](https://wa.me/436602456535).
