# unicorn-binance-trailing-stop-loss Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

## 0.5.0.dev (development stage/unreleased/unstable)
### Added
- Parameter `-- createconfigini` to cli interface
- Parameter `-- createprofilesini` to cli interface
- Parameter `-- openconfigini` to cli interface
- Parameter `-- openprofilesini` to cli interface 
- Parameter `-- example` to cli interface
- `cli.load_examples_ini_from_git_hub()`
### Changed
- ini files are no longer included into setup files of standalone versions
- Messages of test notification are now specific not general

## 0.5.0
### Added
- Warn on updates parameter
- `config` and `pandas` to dependencies
### Changed
- CLI help msg
- Config file path to {home}/.lucit/ubtsl_*.ini
### Fixed
- Ignore missing ubtsl_profile.ini if test is not None
- `Optional` bracket in `manager.get_exchange_info()`
- Using `\` as path separator in windows

## 0.4.2
### Fixed
- Module name for console_scripts in setup.py

## 0.4.1
### Fixed
- Installation via PIP on Windows

## 0.4.0
### Changed
- Many updates in the command line interface `ubtsl`

## 0.3.0
### Added
- Parameter `test` to lib and cli. Supported mode is "notification" to test email and telegram notifications.
- Parameter `print_notificatons`. If True the lib is printing user friendly information to terminal. 
- Count profit to CLI interface
- General output to CLI interface
### Changed
- Returning order details instead of text msg to callback_finished function
### Fixed
- Control notification settings to avoid exceptions

## 0.2.0
CLI update

## 0.1.2
General updates

## 0.1.1
General updates

## 0.1.0
Init