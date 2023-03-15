import sys
import os
from PySide2.QtGui import QPixmap
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal as pyqtSignal
import os, subprocess, sys

os.environ['QT_MAC_WANTS_LAYER'] = '1'
from PySide2.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QTableView,
    QMainWindow, QWidget, QPushButton, QComboBox, QLabel, QListWidget, QTableWidget,
    QFileDialog, QFrame, QMessageBox, QTableWidgetItem, QStyle, QPlainTextEdit
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


class BrazzersManualMainWindow(QWidget):
    def __init__(self, x_pos_parent_window, y_pos_parent_window, width_parent_window):
        super().__init__()
        

        self.x_pos_parent_window = x_pos_parent_window
        self.y_pos_parent_window = y_pos_parent_window
        self.width_parent_window = width_parent_window

        self.setWindowTitle("BRAZZERS - Manual Edition V0.5!")
        self.resize(1000, 600)

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
        self.brazzers_table = QTableWidget()
        self.brazzers_table.setColumnCount(15)
        self.brazzers_table.setHorizontalHeaderLabels(["Nr.", "Site", "PS1", "PS2", "PS3", "PS4",
                                                      "PS5", "PS6", "PS7", "PS8", "PS9", "PS10",
                                                      "title", "loc", "link"])

        header = self.brazzers_table.horizontalHeader()

        #% Define the function which his executed, when cell was clicked !
        self.brazzers_table.cellClicked.connect(self.cell_was_clicked)

        self.brazzers_table_layout.addWidget(self.brazzers_table)

        #% ComboBoxes_layout
        self.comboboxes_complete_layout = QVBoxLayout()
        
        #% Layout for the site
        self.site_layout = QHBoxLayout()
        # self.site_layout.setAlignment(Qsortedt.AlignLeft)
        self.site_label = QLabel("Site: ")
        self.combobox_site = QComboBox()
        
        self.site_layout.addWidget(self.site_label)
        self.site_layout.addWidget(self.combobox_site
                                   )
        #% Layout for the PS1
        self.PS1_layout = QHBoxLayout()
        # self.PS1_layout.setAlignment(Qt.AlignLeft)
        self.PS1_label = QLabel("PS1: ")
        self.combobox_PS1 = QComboBox()
        self.PS1_layout.addWidget(self.PS1_label)
        self.PS1_layout.addWidget(self.combobox_PS1)

        #% Layout for the PS2
        self.PS2_layout = QHBoxLayout()
        self.PS2_label = QLabel("PS2: ")
        # self.PS2_layout.setAlignment(Qt.AlignLeft)
        self.combobox_PS2 = QComboBox()
        self.PS2_layout.addWidget(self.PS2_label)
        self.PS2_layout.stretch(1)
        self.PS2_layout.addWidget(self.combobox_PS2)

        #% Layout for the Title
        self.title_layout = QHBoxLayout()
        self.title_label = QLabel("Title: ")
        # self.title_layout.setAlignment(Qt.AlignLeft)
        self.combobox_title = QComboBox()
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.combobox_title)

        #% Layout for load_and_play_buttons
        self.load_play_and_close_button_layout = QHBoxLayout()
        self.load_button = QPushButton("Load csv-file")
        self.load_button.clicked.connect(self.load_csv_file)
        self.play_button = QPushButton("Play file")
        self.play_button.clicked.connect(self.play_file)
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        self.load_play_and_close_button_layout.addWidget(self.load_button)
        self.load_play_and_close_button_layout.addWidget(self.play_button)
        self.load_play_and_close_button_layout.addWidget(self.close_button)

        #% Layout for the Output of the (possible) terminal statements...
        self.text_statements_layout = QVBoxLayout()
        self.output_textbox = QPlainTextEdit()
        text = "Welcome to brazzers db"
        self.output_textbox.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 15px")
        self.output_textbox.appendPlainText(text)
        self.text_statements_layout.addWidget(self.output_textbox)


        #% Add the single components to the layout
        self.comboboxes_complete_layout.addLayout(self.site_layout)
        self.comboboxes_complete_layout.addLayout(self.PS1_layout)
        self.comboboxes_complete_layout.addLayout(self.PS2_layout)
        self.comboboxes_complete_layout.addLayout(self.title_layout)
        self.comboboxes_complete_layout.addLayout(self.load_play_and_close_button_layout)
        self.comboboxes_complete_layout.addLayout(self.text_statements_layout)

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
        # dummy_widget = QWidget()
        self.complete_layout.addLayout(self.brazzers_logo_site_logo_layout)
        self.complete_layout.addLayout(self.brazzers_table_and_comboxes_layout)#
        self.complete_layout.addLayout(self.complete_link_layout)
        # dummy_widget.setLayout(self.complete_layout)
        # self.setCentralWidget(dummy_widget)
        self.setLayout(self.complete_layout)

    #% Define the methods of the buttons etc....

    def load_csv_file(self):

        self.csv_dir = QFileDialog.getExistingDirectory(
            parent=None,
            caption="Select directory of csv-file",
            # directory="",
        )

        if self.csv_dir == "":
            return
            

        csv_file = pathlib.Path(self.csv_dir) / "df_final_13_03_23.csv"
        # csv_file = pathlib.Path(self.csv_dir) / "df_final_my_db_py_22_04_2022.csv"
        
        print(f"Loading {csv_file} ... ")
        self.loaded_csv_df = pd.read_csv(csv_file)
        # print(self.loaded_csv_df.head())

        self.brazzers_table.setColumnWidth(0, 50)
        self.brazzers_table.setColumnWidth(1, 130)

        #% Filling the table with the content of the csv-file
        # for rows, columns in self.loaded_csv_df.iterrows():
        #     rows = self.brazzers_table.rowCount()
        #     self.brazzers_table.insertRow(rows)
        #     for num, data in enumerate(columns):
        #         self.brazzers_table.setItem(rows, num, QTableWidgetItem(str(data)))
        self.fill_brazzers_table(self.loaded_csv_df)


        #% Filling Combobox of "Site"
        self.site_list_unique = self.loaded_csv_df['Site'].unique()
        self.site_list_sorted = sorted(list(self.site_list_unique))
        self.site_list_sorted = [lf.lstrip() for lf in self.site_list_sorted]
        self.site_list_sorted.insert(0, "== All Sites ==")
        # print('Sorted list: ', self.site_list_sorted)

        for lf, i in zip(self.site_list_sorted, range(len(self.site_list_sorted)+1)):
            self.combobox_site.addItem(lf)
            self.combobox_site.setItemData(i, Qt.AlignRight)
        self.combobox_site.setFixedWidth(160)
        self.combobox_site.currentTextChanged.connect(self.site_changed)

        #% Filling the ComboBox "PS1"
        self.ps1_list_unique = self.loaded_csv_df['PS1'].unique()
        self.ps1_list_sorted = sorted(list(self.ps1_list_unique))
        self.ps1_list_sorted = [lf.lstrip() for lf in self.ps1_list_sorted]
        self.ps1_list_sorted.insert(0, "== All PS1 ==")
        # print('Sorted PS1-list: ', self.ps1_list_sorted)
        for lf in sorted(self.ps1_list_sorted):
            self.combobox_PS1.addItem(lf)  
        for lf, i_ps1 in zip(self.ps1_list_sorted, range(len(self.ps1_list_sorted)+1)):
            self.combobox_PS1.addItem(lf)    
            self.combobox_PS1.setItemData(i_ps1, Qt.AlignHCenter)

        
        #% Filling the ComboBox "PS2" 
        self.ps2_list_unique = self.loaded_csv_df['PS2'].unique()
        self.ps2_list_sorted = sorted(list(self.ps2_list_unique))
        self.ps2_list_sorted = [lf.lstrip() for lf in self.ps2_list_sorted]
        self.ps2_list_sorted.insert(0, "== All PS2 ==")

        for lf in sorted(self.ps2_list_sorted):
            self.combobox_PS2.addItem(lf)  
        for lf, i_ps2 in zip(self.ps2_list_sorted, range(len(self.ps2_list_sorted)+1)):
            self.combobox_PS2.addItem(lf)    
            self.combobox_PS2.setItemData(i_ps2, Qt.AlignHCenter)
        
        self.combobox_PS1.setFixedWidth(160)

        #% Filling the ComboBox "PS2" and adjust it with the max_width of text-entry
        
    
        self.combobox_PS2.setFixedWidth(160)

        # self.combobox_title.setFixedWidth(160)

        # rows = 0

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.brazzers_table.item(row, 0)  
        ### look at the second entry! Because it is 0, python gives the column!

        self.ID_row = item.text()
        print('selected row :', self.ID_row)
        self.selected_file = self.loaded_csv_df.iloc[int(self.ID_row)]['Link']
        self.selected_site_for_picture = self.loaded_csv_df.iloc[int(self.ID_row)]['Site']
        self.selected_title = self.loaded_csv_df.iloc[int(self.ID_row)]['Title']

        print('Link: \n', self.selected_file)
        print('Selected site: \n', self.selected_site_for_picture)
        print('Selected title: \n', self.selected_title)
        self.link_text.setText(self.selected_file)

        name_tmp = self.selected_site_for_picture.replace(" ", "_").lower() + ".png"
        path_folder_site_pictures = "/Users/joerg/repos/braz/site_pictures"
        path_to_picture = os.path.join(path_folder_site_pictures, name_tmp)
        print('path_to_picture', path_to_picture)
        pixmap = QPixmap(path_to_picture)
        self.label_for_site_picture.setPixmap(pixmap)

    #% function for executing, when the site is changed in the combobox...

    def site_changed(self):
       self.brazzers_table.setRowCount(0)
    #    self.combobox_PS1.clear()
       print('currentText_site: ', self.combobox_site.currentText())
       print('self.loaded_csv_df@site_changed: ', self.loaded_csv_df.head())

       self.df_selected_site = self.loaded_csv_df[self.loaded_csv_df['Site'] == self.combobox_site.currentText()]#['Site']
       self.fill_brazzers_table(self.df_selected_site)
 
    def play_file(self):
        subprocess.call(['open', self.selected_file])

    def fill_brazzers_table(self, selected_df: pd.DataFrame):
        # self.loaded_csv_df = load_csv_df
        
        #% Filling the table with the content of the csv-file
        for rows, columns in selected_df.iterrows():
            rows = self.brazzers_table.rowCount()
            self.brazzers_table.insertRow(rows)
            for num, data in enumerate(columns):
                self.brazzers_table.setItem(rows, num, QTableWidgetItem(str(data)))
        
        print('Debug 1', selected_df)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrazzersManualMainWindow(200, 330, 800)
    window.show()
    sys.exit(app.exec_())