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
    QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QTableView,
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
        self.scaled_brazzers = self.pixmap_brazzers.scaled(self.lbl_brazzers_logo.size() / 6, QtCore.Qt.KeepAspectRatio)
        self.lbl_brazzers_logo.setPixmap(self.scaled_brazzers)
        self.lbl_brazzers_logo.setScaledContents(False)

        #% Setting the values for the site_logo 
        self.lbl_site_logo = QLabel("Site logo")
        self.pixmap = QPixmap("/Users/joerg/repos/braz/braz_manual_edition/zz_series.jpg")
        scaled = self.pixmap.scaled(self.lbl_site_logo.size() / 10, QtCore.Qt.KeepAspectRatio)
        self.lbl_site_logo.setPixmap(scaled)
        self.lbl_site_logo.setScaledContents(False)

        #% Fill the brazzers_and_site_logo_layout
        self.brazzers_logo_site_logo_layout.addWidget(self.lbl_brazzers_logo)
        self.brazzers_logo_site_logo_layout.addStretch(1)
        self.brazzers_logo_site_logo_layout.addWidget(self.lbl_site_logo)

        #% Setting up the QTaable and the control buttons or comboboxes

        #% First: Define QHBoxLayout, so that the alignment of the 
        #% table and the comboboxes are horizontal

        self.brazzers_table_and_comboxes_layout = QHBoxLayout()

        #% QTable-Layout 
        self.brazzers_table_layout = QVBoxLayout()
        self.brazzers_table = QTableView()
        self.brazzers_table_layout.addWidget(self.brazzers_table)

        #% ComboBoxes_layout
        self.comboboxes_complete_layout = QVBoxLayout()
        
        #% Layout for the site
        self.site_layout = QHBoxLayout()
        self.site_label = QLabel("Site: ")
        self.combobox_site = QComboBox()
        self.site_layout.addWidget(self.site_label)
        self.site_layout.addWidget(self.combobox_site
                                   )
        #% Layout for the PS1
        self.PS1_layout = QHBoxLayout()
        self.PS1_label = QLabel("PS1: ")
        self.combobox_PS1 = QComboBox()
        self.PS1_layout.addWidget(self.PS1_label)
        self.PS1_layout.addWidget(self.combobox_PS1)

        #% Layout for the PS2
        self.PS2_layout = QHBoxLayout()
        self.PS2_label = QLabel("PS2: ")
        self.combobox_PS2 = QComboBox()
        self.PS2_layout.addWidget(self.PS2_label)
        self.PS2_layout.addWidget(self.combobox_PS2)

        #% Layout for the Title
        self.title_layout = QHBoxLayout()
        self.title_label = QLabel("Title: ")
        self.combobox_title = QComboBox()
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.combobox_title)

        #% Layout for load_and_play_buttons
        self.load_and_play_button_layout = QHBoxLayout()
        self.load_button = QPushButton("Load csv-file")
        self.play_button = QPushButton("Play file")
        self.load_and_play_button_layout.addWidget(self.load_button)
        self.load_and_play_button_layout.addWidget(self.play_button)


        #% Add the single components to the layout
        self.comboboxes_complete_layout.addLayout(self.site_layout)
        self.comboboxes_complete_layout.addLayout(self.PS1_layout)
        self.comboboxes_complete_layout.addLayout(self.PS2_layout)
        self.comboboxes_complete_layout.addLayout(self.title_layout)
        self.comboboxes_complete_layout.addLayout(self.load_and_play_button_layout)

        #% Add both layout to the brazzers_table_and_comboxes_layout

        self.brazzers_table_and_comboxes_layout.addLayout(self.brazzers_table_layout)
        self.brazzers_table_and_comboxes_layout.addLayout(self.comboboxes_complete_layout)


        #% Add Label for the display of the complete link below the qtable
        self.complete_link_layout = QHBoxLayout()
        self.link_label = QLabel("Link: ")
        self.link_text = QLineEdit("")
        self.complete_link_layout.addWidget(self.link_label)
        self.complete_link_layout.addWidget(self.link_text)


        # Set the hand-made complete layout in a superordinate QWidget called dummy_widget
        dummy_widget = QWidget()
        self.complete_layout.addLayout(self.brazzers_logo_site_logo_layout)
        self.complete_layout.addLayout(self.brazzers_table_and_comboxes_layout)#
        self.complete_layout.addLayout(self.complete_link_layout)
        dummy_widget.setLayout(self.complete_layout)
        self.setCentralWidget(dummy_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrazzersManualMainWindow(200, 330, 800)
    window.show()
    sys.exit(app.exec_())