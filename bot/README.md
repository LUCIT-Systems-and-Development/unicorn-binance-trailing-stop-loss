[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)](https://www.lucit.tech/get-support.html)

[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/releases)
[![Conda Release](https://img.shields.io/conda/vn/conda-forge/unicorn-binance-trailing-stop-loss.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-trailing-stop-loss)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/unicorn-binance-trailing-stop-loss.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-trailing-stop-loss)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-trailing-stop-loss?color=blue)](https://pypi.org/project/unicorn-binance-trailing-stop-loss/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-trailing-stop-loss)](https://pepy.tech/project/unicorn-binance-trailing-stop-loss)
[![License](https://img.shields.io/github/license/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss.svg?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/LICENSE)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_trailing_stop_loss.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_trailing_stop_loss.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues)
[![Unit Tests](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/actions/workflows/unit-tests.yml)
[![Azure Pipelines](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/unicorn-binance-trailing-stop-loss-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=15698&branchName=main)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/Bot.html)
[![Github](https://img.shields.io/badge/source-github-yellow)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow)](https://t.me/unicorndevs)
[![Gitter](https://badges.gitter.im/unicorn-binance-suite/unicorn-binance-trailing-stop-loss.svg)](https://gitter.im/unicorn-binance-suite/unicorn-binance-trailing-stop-loss?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![LUCIT-UBTSL-Banner](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-trailing-stop-loss/master/images/logo/LUCIT-UBTSL-Banner-Readme.png)](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html)

# UNICORN Binance Trailing Stop Loss Bot

[Description](#description) | [Installation](#installation) | [Update](#update) | [Change Log](#change-log) | 
[Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | 
[Bugs](#how-to-report-bugs-or-suggest-improvements) | [Contributing](#contributing) | [Leave a review](#you-want-to-say-thank-you) | 
[Disclaimer](#disclaimer) | [Commercial Support](#commercial-support)

After starting the bot, a stop/loss order is placed and trailed until it is completely fulfilled. If desired, a 
notification can be sent via email and Telegram afterwards.

In addition, there is a [smart entry](https://www.lucit.tech/ubtsl-cli.html#smart-entry) option called 
`jump-in-and-trail`. This offers the possibility to buy spot, future and margin assets with a limit or market order 
and then to trail a stop/loss order until sold.

List of [supported exchanges](https://www.lucit.tech/ubtsl-cli.html#description).

The `UNICORN Binance Trailing Stop Loss Bot` uses the engine of the Python library [`unicorn-binance-trailing-stop-loss`](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html)
and has the exact same interface and configuration setup as the[`UNICORN Binance Trailing Stop Loss CLI`](https://www.lucit.tech/ubtsl-cli.html).
It is the same source code!

The bot only does not require a pre-installed Python environment and can be easily installed on [Windows](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html#windows) 
and [Mac](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html#mac) with a 
setup file. If you already have an installed Python environment, we recommend [installing via PIP](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html#installation-and-upgrade) 
and using the [`UNICORN Binance Trailing Stop Loss CLI`](https://www.lucit.tech/ubtsl-cli.html).

Please read carefully all provided [documentation](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/), our
[disclaimer](#disclaimer) and look in the 
[issues](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues) about known 
problems before using this tool - ***you use it at your own risk!***

If you put this bot on a market, you should stop trading manually on this market yourself!

For more information about the usage [read here](https://www.lucit.tech/ubtsl-cli.html).

Part of ['UNICORN Binance Suite'](https://www.lucit.tech/unicorn-binance-suite.html).

## Description
The Bot and [CLI version](https://www.lucit.tech/ubtsl-cli.html) are absolutely identical, except for the installation 
method and that the Bot version does not require a pre-installed Python environment. It is the same source code! Please 
read the [CLI description](https://www.lucit.tech/ubtsl-cli.html#description) for more information. 

## Installation
### Windows
1. [Download ubtsl_setup.exe](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/releases/latest/download/ubtsl_setup.exe)
from GitHub.
2. Start the downloaded `ubtsl_setup.exe`.
3. Click on `More info`. ![Screenshot_0](https://www.lucit.tech/files/images/dev/ubtsl/bot/windows/step_0.png)
4. Click on `Run anyway`. ![Screenshot_1](https://www.lucit.tech/files/images/dev/ubtsl/bot/windows/step_1.png)
5. Click on `Yes` to confirm. ![Screenshot_2](https://www.lucit.tech/files/images/dev/ubtsl/bot/windows/step_2.png)
6. Read and accept the license. ![Screenshot_3](https://www.lucit.tech/files/images/dev/ubtsl/bot/windows/step_3a.png)
7. Click `Next` 3 times, then click `Install`.
8. Read the following [post installation instructions](https://www.lucit.tech/ubtsl-cli.html#installation).

### Mac
Coming soon! Receive a 
[notification](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html#receive-notifications) on release.

## Update
### Windows
Just start `ubtsl` with the parameter `--installupdate`. Only available in the bot version!

```sh
$ ubtsl --installupdate
```

### Mac
Coming soon! Receive a [notification](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html#receive-notifications) on release.

## Change Log
[https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/CHANGELOG.html](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/CHANGELOG.html)

## Documentation
- [General](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech)
- [Modules](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/unicorn_binance_trailing_stop_loss.html)
- [CLI](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/CLI.html)
- [Bot](https://unicorn-binance-trailing-stop-loss.docs.lucit.tech/Bot.html)

## Project Homepage
[https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss)

## Wiki
[https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/wiki](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/wiki)

## Social
- [Discussions](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-trailing-stop-loss/master/images/misc/watch.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/watchers) 
the repository on [GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss).

Follow us on [Twitter](https://twitter.com/LUCIT_SysDev) or on [Facebook](https://www.facebook.com/lucit.systems.and.development) 
for general news about the [unicorn-binance-suite](https://www.lucit.tech/unicorn-binance-suite.html)!

To receive news (like inspection windows/maintenance) about the Binance API`s subscribe to their telegram groups: 

- [https://t.me/binance_api_announcements](https://t.me/binance_api_announcements)
- [https://t.me/binance_api_english](https://t.me/binance_api_english)
- [https://t.me/Binance_JEX_EN](https://t.me/Binance_JEX_EN)
- [https://t.me/Binance_USA](https://t.me/Binance_USA)
- [https://t.me/TRBinanceTR](https://t.me/TRBinanceTR)
- [https://t.me/BinanceDEXchange](https://t.me/BinanceDEXchange)
- [https://t.me/BinanceExchange](https://t.me/BinanceExchange)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-trailing-stop-loss/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you dont find an issue related to your topic, please open a new [issue](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/issues)!

[Report a security bug!](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/security/policy)

## Contributing
[UNICORN Binance Trailing Stop Loss](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/graphs/contributors)

We ![love](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-trailing-stop-loss/master/images/misc/heart.png) open source!

## You want to say Thank You?
We hope you are enjoying using our libraries and that they are proving to be useful to you. If you have a moment, we would greatly appreciate it if you could leave us a [review on Google](https://g.page/r/CbfHlcs8BfG8EAg/review). Thank you for your support!

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

[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)](https://www.lucit.tech/get-support.html)

***Do you need a developer, operator or consultant?*** [Contact us](https://www.lucit.tech/contact.html) for a non-binding initial consultation!
