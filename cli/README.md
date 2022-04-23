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
$ ubtsl 
usage: UNICORN Binance Trailing Stop Loss CLI 0.1.1 (MIT License) [-h] [--apikey APIKEY] [--apisecret APISECRET] [--exchange EXCHANGE] [--configfile CONFIGFILE] [--keepthreshold KEEPTHRESHOLD] [--limit LIMIT] [--logfile LOGFILE]
                                                                  [--loglevel LOGLEVEL] [--orderside ORDERSIDE] [--ordertype ORDERTYPE] [--profile PROFILE] [--profilesfile PROFILESFILE] [--resetstoplossprice RESETSTOPLOSSPRICE]
                                                                  [--stoplossprice STOPLOSSPRICE] [--symbol SYMBOL]

optional arguments:
  -h, --help            show this help message and exit
  --apikey APIKEY       The API key!
  --apisecret APISECRET
                        The API secret!
  --configfile CONFIGFILE
                        Specify path including filename to the config file. (Ex: `~/config.ini`) If not available it 
                        tries to load a ubtsl_config.ini from the home and the current working directory.
  --exchange EXCHANGE   Exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...
  --keepthreshold KEEPTHRESHOLD
                        Exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...
  --limit LIMIT         Stop/loss limit in integer or percent.
  --logfile LOGFILE     Specify path including filename to the logfile.
  --loglevel LOGLEVEL   Choose a log level (DEBUG, INFO, WARNING, ERROR or CRITICAL). Default is `INFO.
  --orderside ORDERSIDE
                        Specify whether the trailing stop loss should be in buying or selling mode. (Ex: 'buy' or 'sell').
  --ordertype ORDERTYPE
                        Use `limit` or `market`.
  --profile PROFILE     Name of the profile to load from profiles.ini!
  --profilesfile PROFILESFILE
                        Specify path including filename to the profiles file. (Ex: `~/profiles.ini`) If not available 
                        it tries to load a ubtsl_profile.ini from the home and the current working directory.
  --resetstoplossprice RESETSTOPLOSSPRICE
                        Reset the existing stop_loss_price! Usage: True anything else is False!
  --stoplossprice STOPLOSSPRICE
                        Set the starting stop/loss price.
  --symbol SYMBOL       The market symbol as used by Binance.
```

## Example usage
Arguments defined in the CLI overrule values from the loaded profile!

```
$ ubtsl --profile LUNAUSDT_SELL --configfile yourconfig.ini --stoplossprice 88.50 --limit 0.5%
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
