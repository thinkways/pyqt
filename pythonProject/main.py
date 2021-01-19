import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
