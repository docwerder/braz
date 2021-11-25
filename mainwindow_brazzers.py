from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import  *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import itertools
import pathlib

from load_brazzers_database import load_bra_db
import sys

import pandas as pd
from os import path
import os, subprocess, sys
from PyQt5.uic import loadUiType

import search_window_file as search_window

FORM_CLASS, _=loadUiType(path.join(path.dirname('__file__'),"mainwindow_brazzers.ui"))

import sqlite3

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        #self.NAVIGATE()


    def Handel_Buttons(self):
        #self.refresh_btn.clicked.connect(self.GET_DATA)
        #self.load_df_button.clicked.connect(self.LOAD_DF)

        # New version. Try to load a csv-file into dataframe!
        self.load_df_button.clicked.connect(self.load_csv_file)
        #self.search_btn.clicked.connect(self.SEARCH)
        #self.search_button.clicked.connect(self.SEARCH_BRA_DF)
        #self.search_window_button.clicked.connect(self.open_search_window)
        #self.comboBox_site.currentIndexChanged.connect(self.site_changed)
        #self.comboBox_site.currentTextChanged.connect(self.site_changed)
        #self.comboBox_site.currentTextChanged.connect(self.on_combobox_changed)

        #self.comboBox_title.currentIndexChanged.connect(self.title_changed)
        #self.play_file_button.clicked.connect(self.play_file)
        #self.mycheckBox.setCheckState(Qt.PartiallyChecked)
        #self.check_btn.clicked.connect(self.LEVEL)

    # def LOAD_DF(self):
    #         # dict = {'ps_name': ["Nikki Benz", "Shyla Stylez", "Velicity Von", "Rebecca Moore"],
    #         #         'site': ["big_tits_at_school", "big_tits_at_work", "big_tits_in_uniform", "real_wife_stories"],
    #         #         'score': [90, 40, 80, 98]}
    #         #df = pd.DataFrame(dict)
    #         #print(df)
    #         bra_dir = '/Volumes/WERDERNASX/VIDEOSX/BRAZZERS'
    #         self.bra_db_df = load_bra_db(bra_dir)
    #
    #         #print(self.bra_db_df)
    #         #print('Arbitrary df: \n', df)
    #         rows = 0
    #         # for row_number, row_data in enumerate(df):
    #         self.bra_dir_table.setRowCount(0)
    #
    #         for rows, columns in self.bra_db_df.iterrows():
    #             #print('rows: ', rows)
    #             #print(columns['Site Name'])
    #             self.bra_dir_table.insertRow(rows)
    #             for num, data in enumerate(columns):
    #                 self.bra_dir_table.setItem(rows, num, QTableWidgetItem(str(data)))
    #
    #
    #         self.combobox_site = comboBox_site(self)
    #         print('spalten:', self.bra_db_df['Site Name'].unique())
    #         self.combobox_site.addItems(self.bra_db_df['Site Name'].unique())
    #
    #         self.bra_dir_table.setCellWidget(0, 0, self.combobox_site)
    #
    #
    #         # Code below should work ...
    #         # for rows, columns in df.iterrows():
    #         #     # print('rows: ', rows)
    #         #     # print(columns['ps_name'])
    #         #     self.bra_dir_table.insertRow(rows)
    #         #     for num, data in enumerate(columns):
    #         #         self.bra_dir_table.setItem(rows, num, QTableWidgetItem(str(data)))
    #
    #             #print('row_number: \t', df[row_number])
    #             #print('row_data: \t', row_data)
    #             #self.bra_dir_table.insertRow(rows)
    #             #for columns, df[rows] in enumerate(df):
    #              #   self.bra_dir_table.setItem(columns, df[rows], QTableWidgetItem(str(df[rows])))

    def load_csv_file(self):

        self.csv_dir = QtWidgets.QFileDialog.getExistingDirectory(
            parent=None,
            caption="Select directory of csv-file",
            directory="",
        )

        if self.csv_dir == "":
            return

        csv_file = pathlib.Path(self.csv_dir) / "bra_final_py.csv"

        print(f"Loading {csv_file} ... ")
        self.loaded_csv_df = pd.read_csv(csv_file)
        #print('Index: ', self.loaded_csv_df.index)


        # bra_dir = '/Volumes/WERDERNASX/VIDEOSX/BRAZZERS'
        # self.bra_db_df = load_bra_db(bra_dir)
        rows = 0

        # # for row_number, row_data in enumerate(df):
        #self.bra_dir_table.setRowCount(0)


        # Set Width of the columns within the QTableWidget
        #self.bra_dir_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.bra_dir_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.bra_dir_table.setColumnWidth(0, 50)
        self.bra_dir_table.setColumnWidth(1, 130)




        #print('reduced_df: \n', self.loaded_csv_df_reduced)
        for rows, columns in self.loaded_csv_df.iterrows():
            rows = self.bra_dir_table.rowCount()
            self.bra_dir_table.insertRow(rows)
            for num, data in enumerate(columns):
                self.bra_dir_table.setItem(rows, num, QTableWidgetItem(str(data)))
        #
        #
        #self.comboBox_site = comboBox(self)
        #self.comboBox_site.clear()
        #print('spalten:', self.loaded_csv_df['Site'].unique())

        # Populate the Combobox site
        self.site_list_unique = self.loaded_csv_df['Site'].unique()
        self.site_list_unique = list(self.site_list_unique)
        self.site_list_unique.insert(0, "All Sites")
        for lf in self.site_list_unique:
            self.comboBox_site.addItem(lf)

        # Populate the combobox ps1
        self.ps1_list_unique = self.loaded_csv_df['PS1'].unique()
        self.ps1_list_unique = list(self.ps1_list_unique)
        self.ps1_list_unique.insert(0, "All Pornstars")
        for lf in self.ps1_list_unique:
            self.comboBox_ps1.addItem(lf)



        #[self.comboBox_site.addItem(x) for x in self.loaded_csv_df['Site'].unique()]
        #self.comboBox_site.insertItem(0, 'All Sites')
        #self.comboBox_site.addItems(self.site_list_unique)

        self.comboBox_site.currentTextChanged.connect(self.site_changed)
        self.comboBox_ps1.currentIndexChanged.connect(self.ps1_changed)
        # self.bra_dir_table.setCellWidget(0, 0, self.combobox_site)
        #


    def GET_DATA(self):


                
        # Connect to Sqlite3 database and fill GUI table with data
        db = sqlite3.connect("parts.db")
        cursor = db.cursor()

        command = ''' SELECT * FROM parts_table'''

        result = cursor.execute(command)

        #self.df = pd.read_sql_query(command, db)
        # self.bra_dir_table = QTableWidget(parent=self)
        # self.bra_dir_table.setColumnCount(len(self.df.columns))
        # self.bra_dir_table.setRowCount(len(self.df.index))index

        # for i in range(len(self.df.index)):
        #     for j in range(len(self.df.columns)):
        #         self.data_only = self.df.iloc[i,j]
        #         print(self.data_only)
        #
        #         #self.inventory_table.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))
        #         self.inventory_table.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i,j])))
        self.bra_dir_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.bra_dir_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.bra_dir_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))



        # Display references number and type number in statistics tab

        cursor2 = db.cursor()
        cursor3 = db.cursor()

        parts_nbr = ''' SELECT COUNT (DISTINCT PartName) from parts_table'''
        ref_nbr = ''' SELECT COUNT (DISTINCT Reference) from parts_table'''

        result_ref_nbr = cursor2.execute(ref_nbr)
        result_parts_nbr = cursor3.execute(parts_nbr)

        self.lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
        self.lbl_parts_nbr.setText(str(result_parts_nbr.fetchone()[0]))


        # Display 4 results: Min, Max Number of hole in addition to their respective reference names

        cursor4 = db.cursor()
        cursor5 = db.cursor()

        min_hole = ''' SELECT MIN(NumberOfHoles), Reference, PartName from parts_table'''
        max_hole = ''' SELECT MAX(NumberOfHoles), Reference from parts_table'''

        result_min_hole = cursor4.execute(min_hole)
        result_max_hole = cursor5.execute(max_hole)

        r1 = result_min_hole.fetchone()
        r2 = result_max_hole.fetchone()
        print(r1)
        print(r2)
        self.lbl_min_hole.setText(str(r1[0]))
        self.lbl_max_hole.setText(str(r2[0]))

        self.lbl_min_hole_2.setText(str(r1[1]))
        self.lbl_max_hole_2.setText(str(r2[1]))

    def SEARCH(self):
        db = sqlite3.connect("parts.db")
        cursor = db.cursor()

        
        r = int(self.count_filter_txt.text())
        command = ''' SELECT * FROM parts_table WHERE count <=?'''
        print(command)
        result = cursor.execute(command,[nbr])
        self.bra_dir_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.bra_dir_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.bra_dir_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def SEARCH_BRA_DF(self):
        #print('going into...')
        bra_dir = '/Volumes/WERDERNASX/VIDEOSX/BRAZZERS'
        self.bra_db_df = load_bra_db(bra_dir)

        self. bra_dir_table .setRowCount(0)
        self. bra_dir_table .setRowCount(0)

        for rows, columns in self.bra_db_df.iterrows():
            #print('rows: ', rows)
            #print(columns['Site Name'])
            self.bra_dir_table.insertRow(rows)
            for num, data in enumerate(columns):
                self.bra_dir_table.setItem(rows, num, QTableWidgetItem(str(data)))

        # fill the comboBox with the unique values of site name
        [self.comboBox_site.addItem(x)for x in self.bra_db_df['Site Name'].unique()]
        print('veränderung...')
    def open_search_window(self):
        # self.search_window = search_window.Search_window()
        # self.search_window.show()
        self.search_window = search_window.Search_window_new()
        self.search_window.show()

    def site_changed(self):
        self.bra_dir_table.setRowCount(0)
        #self.comboBox_ps1.clear()
        self.ps1 = self.loaded_csv_df[self.loaded_csv_df['Site'] == self.comboBox_site.currentText()]['PS1']
        [self.comboBox_ps1.addItem(x) for x in self.ps1.unique()]
        print('site changed to: ', self.comboBox_site.currentText())
        selected_site = self.comboBox_site.currentText()
        if selected_site == "All Sites":
            for rows, columns in self.loaded_csv_df.iterrows():
                rows = self.bra_dir_table.rowCount()
                self.bra_dir_table.insertRow(rows)
                for num, data in enumerate(columns):
                    self.bra_dir_table.setItem(rows, num, QTableWidgetItem(str(data)))
        else:
            self.selected_df_of_selected_site = self.loaded_csv_df[self.loaded_csv_df['Site'] == selected_site]

            rows = 0
            for rows, columns in self.selected_df_of_selected_site.iterrows():
                rows = self.bra_dir_table.rowCount()
                self.bra_dir_table.insertRow(rows)
                for num, data in enumerate(columns):
                    self.bra_dir_table.setItem(rows, num, QTableWidgetItem(str(data)))

    def ps1_changed(self):
        self.bra_dir_table.setRowCount(0)
        self.comboBox_title.clear()

        self.df = self.loaded_csv_df
        #ps_name = "Nikki Benz"

        ps_name = self.comboBox_ps1.currentText()
        # ps_selection = df[((df['PS1'] == "Nikki Benz") | (df['PS2'] == "Nikki Benz"))]
        ps_selection = self.df[((self.df['PS1'] == ps_name) | (self.df['PS2'] == ps_name) | (self.df['PS3'] == ps_name) |
                                (self.df['PS4'] == ps_name) | (self.df['PS5'] == ps_name) | (self.df['PS6'] == ps_name) |
                                (self.df['PS7'] == ps_name) | (self.df['PS8'] == ps_name) | (self.df['PS9'] == ps_name) |
                                (self.df['PS10'] == ps_name))]
        print('Selected pornstar: ', ps_name)
        print('Selected dataframe: ', ps_selection)
        print('Length: ', len(ps_selection))

        # self.title = self.loaded_csv_df[(self.loaded_csv_df['Site'] == self.comboBox_site.currentText()) &
        #                             (self.loaded_csv_df['PS1'] == self.comboBox_ps1.currentText())]['Title']
        # [self.comboBox_title.addItem(x) for x in self.title.unique()]

    def title_changed(self):
        # self.link = self.loaded_csv_df[(self.loaded_csv_df['Site'] == self.comboBox_site.currentText()) &
        #                            (self.loaded_csv_df['PS1'] == self.comboBox_ps1.currentText()) &
        #                            (self.loaded_csv_df['Title'] == self.comboBox_title.currentText())]['Link']
        self.link = self.loaded_csv_df[(self.loaded_csv_df['Site'] == self.comboBox_site.currentText()) &
                                       (self.loaded_csv_df['PS1'] == self.comboBox_ps1.currentText())]


        print(self.link)
        #print(self.textEdit_link.setPlainText(self.link.item()))


    def play_file(self):
        self.path_to_bra_file = self.link.item()
        subprocess.call(['open', self.path_to_bra_file])

    def LEVEL(self):
        db = sqlite3.connect("parts.db")
        cursor = db.cursor()
        command = ''' SELECT Reference, PartName, Count FROM parts_table order by COUNT asc LIMIT 3'''
        result = cursor.execute(command)

        self.table_2.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def NAVIGATE(self):
        db = sqlite3.connect("parts.db")
        cursor = db.cursor()

        command = ''' SELECT * from parts_table'''
        result  = cursor.execute(command)

        val = result.fetchone()

        self.id.setText(str(val[0]))
        self.reference.setText(str(val[1]))
        self.part_name.setText(str(val[2]))
        self.min_area.setText(str(val[3]))
        self.max_area.setText(str(val[4]))
        self.number_of_holes.setText(str(val[5]))
        self.min_diameter.setText(str(val[6]))
        self.max_diameter.setText(str(val[7]))
        self.count.setValue(val[8])

class comboBox_site(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        #self.setStyleSheet('font-size: 25px')
        #self.addItems(['Microsoft', 'Facebook', 'Apple', 'Google'])

        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())
        # return self.currentText()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()
    #sys(app.exec_())

if __name__ == '__main__':
    main()



#import sqlite3