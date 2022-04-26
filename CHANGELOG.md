# unicorn-binance-trailing-stop-loss Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

## 0.4.2.dev (development stage/unreleased/unstable)
### Added
- Warn on updates parameter
### Fixed
- Ignore mssing ubtsl_profile.ini if test is not None

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