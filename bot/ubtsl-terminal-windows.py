#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: bot/ubtsl-terminal.py
#
# Part of ‘UNICORN Binance Trailing Stop Loss’
# Project website: https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-trailing-stop-loss
# Documentation: https://unicorn-binance-trailing-stop-loss.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-trailing-stop-loss
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

import sys
import time
import win32gui

from PyQt5.QtCore import QProcess, Qt
from PyQt5.QtGui import QWindow, QIcon, QFont
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMdiArea, QSplitter, QTextBrowser
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from win32com import client
from win32gui import GetWindowText, EnumWindows,SetForegroundWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p = QProcess()
        self.layout = QVBoxLayout()
        self.mdi = QMdiArea()
        self.mainSplitter = QSplitter(Qt.Vertical)
        self.setCentralWidget(self.mainSplitter)
        self.mainSplitter.addWidget(QTextBrowser())
        self.initUI()

    def initUI(self):
        self.runExe()
        EnumWindows(self.set_cmd_to_foreground, None)
        hwnd1 = win32gui.GetForegroundWindow()
        #hwnd1 = win32gui.FindWindow(None, "C:\\Windows\\system32\\calc.exe")
        print(hwnd1)
        window = QWindow.fromWinId(hwnd1)
        container_widge = self.createWindowContainer(window, self)
        container_widge.setFocusPolicy(Qt.TabFocus)
        container_widge.setFocus()
        container_widge.setWindowTitle("ain")
        container_widge.setFont(QFont("Times New Roman"))
        container_widge.setGeometry(500, 500, 450, 400)
        #container_widge.setFocusPolicy()
        container_widge.activateWindow()
        container_widge.acceptDrops()
        container_widge.grabMouse()
        container_widge.setMouseTracking(True)
        self.mainSplitter.addWidget(container_widge)
        self.showMaximized()
        #self.setGeometry(200, 200, 700, 700)
        #self.show()

    def runExe(self):
        shell.run("cmd.exe")
        time.sleep(1)

    def set_cmd_to_foreground(self, hwnd, extra):
        if "cmd.exe" in GetWindowText(hwnd):
            print(hwnd)
            SetForegroundWindow(hwnd)
            return

    def run_script(self, shell, scripts):
        shell.SendKeys(scripts+"{ENTER}")

if __name__ == '__main__':
    shell = client.Dispatch("WScript.Shell")
    app = QApplication(sys.argv)
    ex = Example()
    #ex.run_script(shell, "python -m pip list")
    #ex.show()
    sys.exit(app.exec_())
