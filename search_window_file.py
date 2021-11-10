from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import  *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType

ui_path = path.join(path.dirname(__file__),"search_window.ui")
FORM_CLASS, _ = loadUiType(ui_path)

class Search_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Window")
        self.label = QtWidgets.QLabel("Build the search mask....")
        self.setCentralWidget(self.label)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

class Search_window_new(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Search_window_new, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
