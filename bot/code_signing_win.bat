::
:: File: bot/code_signing_win.bat
::
:: Part of ‘UNICORN Binance Trailing Stop Loss’
:: Project website: https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html
:: Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
:: Documentation: https://unicorn-binance-trailing-stop-loss.docs.lucit.tech
:: PyPI: https://pypi.org/project/unicorn-binance-trailing-stop-loss
::
:: Author: LUCIT Systems and Development
::
:: Copyright (c) 2022-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
:: All rights reserved.
::
:: Permission is hereby granted, free of charge, to any person obtaining a
:: copy of this software and associated documentation files (the
:: "Software"), to deal in the Software without restriction, including
:: without limitation the rights to use, copy, modify, merge, publish, dis-
:: tribute, sublicense, and/or sell copies of the Software, and to permit
:: persons to whom the Software is furnished to do so, subject to the fol-
:: lowing conditions:
::
:: The above copyright notice and this permission notice shall be included
:: in all copies or substantial portions of the Software.
::
:: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
:: OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
:: ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
:: SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
:: WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
:: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
:: IN THE SOFTWARE.

:: Env path: "c:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\"

signtool.exe sign /a /fd SHA256 Z:\unicorn-binance-trailing-stop-loss\dist\ubtsl_setup.exe
signtool.exe timestamp /tr http://timestamp.sectigo.com /td SHA256 Z:\unicorn-binance-trailing-stop-loss\dist\ubtsl_setup.exe