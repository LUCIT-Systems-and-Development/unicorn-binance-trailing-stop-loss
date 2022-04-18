# UNICORN Binance Trailing Stop Loss CLI
## Description
The CLI interface is installed by the PIP installation on Linux systems:
```
$ ubtsl 
usage: UNICORN Binance Trailing Stop Loss CLI 0.1.1 [-h] [--apikey APIKEY] [--apisecret APISECRET] [--exchange EXCHANGE] [--keepthreshold KEEPTHRESHOLD] [--limit LIMIT] [--logfile LOGFILE] [--orderside ORDERSIDE]
                                                    [--ordertype ORDERTYPE] [--profile PROFILE] [--profilesfile PROFILESFILE] [--resetstoplossprice RESETSTOPLOSSPRICE] [--configfile CONFIGFILE] [--stoplossprice STOPLOSSPRICE]
                                                    [--symbol SYMBOL] [--loglevel LOGLEVEL]

optional arguments:
  -h, --help            show this help message and exit
  --apikey APIKEY       The API key!
  --apisecret APISECRET
                        The API secret!
  --exchange EXCHANGE   Exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...
  --keepthreshold KEEPTHRESHOLD
                        Exchange: binance.com, binance.com-margin, binance.com-isolated_margin, ...
  --limit LIMIT         Stop/loss limit in integer or percent.
  --logfile LOGFILE     Specify path including filename to the logfile.
  --orderside ORDERSIDE
                        Specify whether the trailing stop loss should be in buying or selling mode. (Ex: 'buy' or 'sell').
  --ordertype ORDERTYPE
                        Use `limit` or `market`.
  --profile PROFILE     Name of the profile to load from profiles.ini!
  --profilesfile PROFILESFILE
                        Specify path including filename to the profiles file. (Ex: `~/profiles.ini`) If not available it tries to load a profile.ini from the current working directory.
  --resetstoplossprice RESETSTOPLOSSPRICE
                        Reset the existing stop_loss_price! Usage: True anything else is False!
  --configfile CONFIGFILE
                        Specify path including filename to the config file. (Ex: `~/config.ini`) If not available it tries to load a config.ini from the current working directory.
  --stoplossprice STOPLOSSPRICE
                        Set the starting stop/loss price.
  --symbol SYMBOL       The market symbol as used by Binance.
  --loglevel LOGLEVEL   Choose a log level (DEBUG, INFO, WARNING, ERROR or CRITICAL). Default is `INFO.

additional information:
    Home: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
```

## Example
Arguments defined in the CLI overrule values from the loaded profile

```
ubtsl --profile LUNAUSDT_SELL --configfile yourconfig.ini --stoplossprice 88.50 --limit 0.5%
```

## Examples
- [example_ubtsl_config.ini](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/cli/example_ubtsl_config.ini)
- [example_ubtsl_profiles.ini](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss/blob/master/cli/example_ubtsl_profiles.ini)
