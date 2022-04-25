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

# UNICORN Binance Trailing Stop Loss CLI

## Description
The CLI interface `ubtsl` is installed during the 
[installation](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html#installation-and-upgrade) 
of `unicorn-binance-trailing-stop-loss` with PIP and is used to interact with the 
[`UNICORN Binance Tailing Stop Loss`](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html) library.

After startup `ubtsl` tries to load a 
[`ubtsl_config.ini`](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/cli/example_ubtsl_config.ini) 
and a 
[`ubtsl_profiles.ini`](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/cli/example_ubtsl_profiles.ini) 
file from the home and the current working directory.

Test the notification settings:

```
$ ubtsl --test notification
```

If profiles are available, they can be activated with the `--profiles` parameter at startup. Any CLI parameters will 
overwrite predefined values from the profile.

Once the tool is started, it trailes the stop/loss order until it is completely fulfilled and then calls the function 
passed with the `callback_finished` parameter.

```
$ ubtsl --help
usage: UNICORN Binance Trailing Stop Loss CLI 0.4.0 (MIT License) [-h] [-ak APIKEY] [-as APISECRET]
                                                                  [-cf CONFIGFILE] [-cu] [-e EXCHANGE] [-n ENGINE]
                                                                  [-k KEEPTHRESHOLD] [-lf LOGFILE] [-ll LOGLEVEL]
                                                                  [-os ORDERSIDE] [-ot ORDERTYPE] [-pf PROFILE]
                                                                  [-pff PROFILESFILE] [-r RESETSTOPLOSSPRICE]
                                                                  [-l STOPLOSSLIMIT] [-p STOPLOSSPRICE]
                                                                  [-sl STOPLOSSSTARTLIMIT] [-s SYMBOL] [-t TEST]
                                                                  [-v]

optional arguments:
  -h, --help            show this help message and exit
  -ak APIKEY, --apikey APIKEY
                        the API key
  -as APISECRET, --apisecret APISECRET
                        the API secret
  -cf CONFIGFILE, --configfile CONFIGFILE
                        specify path including filename to the config file (ex: `~/my_config.ini`). if not provided ubtsl tries to load a `ubtsl_config.ini` from the home and the current working directory.
  -cu, --checkupdate    check if update is available
  -e EXCHANGE, --exchange EXCHANGE
                        exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...
  -n ENGINE, --engine ENGINE
                        default: `trail` options: - `jump-in-and-trail` to place a market buy order and trail
  -k KEEPTHRESHOLD, --keepthreshold KEEPTHRESHOLD
                        exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...
  -lf LOGFILE, --logfile LOGFILE
                        specify path including filename to the logfile
  -ll LOGLEVEL, --loglevel LOGLEVEL
                        default: INFO available log levels: DEBUG, INFO, WARNING, ERROR and CRITICAL
  -os ORDERSIDE, --orderside ORDERSIDE
                        specify whether the trailing stop loss should be in buying or selling mode. (ex: 'buy' or 'sell')
  -ot ORDERTYPE, --ordertype ORDERTYPE
                        use `limit` or `market`
  -pf PROFILE, --profile PROFILE
                        name of the profile to load from ubtsl_profiles.ini!
  -pff PROFILESFILE, --profilesfile PROFILESFILE
                        specify path including filename to the profiles file (ex: `~/my_profiles.ini`). if not available ubtsl tries to load a ubtsl_profile.ini from the home and the current working directory
  -r RESETSTOPLOSSPRICE, --resetstoplossprice RESETSTOPLOSSPRICE
                        reset the existing stop_loss_price! usage: True anything else is False
  -l STOPLOSSLIMIT, --stoplosslimit STOPLOSSLIMIT
                        stop/loss limit in float or percent
  -p STOPLOSSPRICE, --stoplossprice STOPLOSSPRICE
                        set the start stop/loss price as float value
  -sl STOPLOSSSTARTLIMIT, --stoplossstartlimit STOPLOSSSTARTLIMIT
                        set the start stop/loss limit in float or percent. (only used in "jump-in-and-trail"
  -s SYMBOL, --symbol SYMBOL
                        the market symbol as used by binance
  -t TEST, --test TEST  use this to test specific systems like "notification". if test is not None the engine will NOT start! It only tests!
  -v, --version         show the program version, which is `0.3.0` by the way :)
```

## Example usage
Arguments defined in the CLI overrule values from the loaded profile!

Check if a new update is available:

```
$ ubtsl --checkupdate
```

Show program version:

```
$ ubtsl --version
```

Start with profile "LUNAUSDT_SELL" and overwrite the stoplosslimit:

```
$ ubtsl --profile LUNAUSDT_SELL --stoplosslimit 0.5%
```

## Examples
- [example_ubtsl_config.ini](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/cli/example_ubtsl_config.ini)
- [example_ubtsl_profiles.ini](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/cli/example_ubtsl_profiles.ini)

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
