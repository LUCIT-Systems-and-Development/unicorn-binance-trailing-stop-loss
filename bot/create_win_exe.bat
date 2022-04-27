echo Install latest ubtsl wheel
py -m pip install "Z:\unicorn-binance-trailing-stop-loss\dist\unicorn_binance_trailing_stop_loss-0.5.0-py3-none-any.whl" --upgrade
echo Creating ubtsl.exe ...
cd bot
pyinstaller ubtsl.py
cd ..