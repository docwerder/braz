import sys
import os
from PySide2.QtGui import QPixmap
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal as pyqtSignal
os.environ['QT_MAC_WANTS_LAYER'] = '1'
from PySide2.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit,
    QMainWindow, QWidget, QPushButton, QComboBox, QLabel, QListWidget,
    QFileDialog, QFrame, QMessageBox
)
#from emat_mfl_combined.applications.pdw_upload.analysis_tools.path2proj import Path2ProjAnomaliesGeneral
import pathlib
import os
import pandas as pd
from tabulate import tabulate

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class BrazzersManualMainWindow(QMainWindow):
    def __init__(self, x_pos_parent_window, y_pos_parent_window, width_parent_window):
        super().__init__()
        

        self.x_pos_parent_window = x_pos_parent_window
        self.y_pos_parent_window = y_pos_parent_window
        self.width_parent_window = width_parent_window

        self.setWindowTitle("BRAZZERS - Manual Edition V0.5!")
        #self.setFixedSize(1000, 700)

        ### Define the layout ####
        
        # Create the complete layout
        self.complete_layout = QVBoxLayout()

        # Layout for brazzers_label and Site_picture
        self.brazzers_logo_site_logo_layout = QHBoxLayout()

        # Define label for brazzers_logo and site_logo. First step: Default png-picture!
        self.lbl_brazzers_logo = QLabel()
        #self.lbl_brazzers_logo.setStyleSheet("font-size: 18px;" "color: rgb(44, 44, 126);")
        
        self.pixmap_brazzers = QPixmap("/Users/joerg/repos/braz/braz_manual_edition/brazzers.png")
        self.scaled_brazzers = self.pixmap_brazzers.scaled(self.lbl_brazzers_logo.size() / 4, QtCore.Qt.KeepAspectRatio)
        self.lbl_brazzers_logo.setPixmap(self.scaled_brazzers)
        self.lbl_brazzers_logo.setScaledContents(False)

        # Setting the values for the site_logo 
        self.lbl_site_logo = QLabel("Site logo")
        self.pixmap = QPixmap("/Users/joerg/repos/braz/braz_manual_edition/zz_series.jpg")
        scaled = self.pixmap.scaled(self.lbl_site_logo.size() / 4, QtCore.Qt.KeepAspectRatio)
        self.lbl_site_logo.setPixmap(scaled)
        self.lbl_site_logo.setScaledContents(False)

        # Fill the brazzers_and_site_logo_layout
        self.brazzers_logo_site_logo_layout.addWidget(self.lbl_brazzers_logo)
        self.brazzers_logo_site_logo_layout.addStretch(1)
        self.brazzers_logo_site_logo_layout.addWidget(self.lbl_site_logo)


        # Set the hand-made complete layout in a superordinate QWidget called dummy_widget
        dummy_widget = QWidget()
        self.complete_layout.addLayout(self.brazzers_logo_site_logo_layout)
        dummy_widget.setLayout(self.complete_layout)
        self.setCentralWidget(dummy_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrazzersManualMainWindow(200, 330, 800)
    window.show()
    sys.exit(app.exec_())