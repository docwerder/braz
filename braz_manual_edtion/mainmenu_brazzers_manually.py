import sys
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout,
    QFormLayout, QGridLayout, QTableWidget,
    QComboBox,
    QPushButton, QCheckBox, QListWidget, QFrame,
    QWidget, QMainWindow, QLineEdit, QLabel
)
from PySide2.QtGui import QFontMetrics
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)

class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)

class MainWindowBrazzers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main menu manually V0.5")

        # #############################################
        #  Define the layout
        # #############################################
        # Create the complete layout
        self.complete_layout = QVBoxLayout()

        # Layout for label_picture and site_pictures
        self.label_pic_and_site_pictures = QHBoxLayout()
        self.braz_pic = QLabel("Label braz")
        print('width of label: ', self.braz_pic.width())
        self.braz_pic.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        #self.braz_pic.setFixedWidth(480)
        #self.braz_pic.setFixedHeight(640)
        #self.braz_pic.setStyleSheet("background-color: rgb(162, 162, 162)")
        self.braz_pixmap = QPixmap("/Users/joerg/repos/braz/site_pictures/brazzers.png")
        scaled_braz = self.braz_pixmap.scaled(self.braz_pic.size() / 4, QtCore.Qt.KeepAspectRatio)
        self.braz_pic.setPixmap(scaled_braz)
        self.braz_pic.setScaledContents(False)

        self.label_for_site_picture = QLabel("Site_picture")
        #self.label_for_site_picture.setStyleSheet("background-color: rgb(255, 255, 255)")
        name_tmp = "big_tits_in_uniform.png"
        path_folder_site_pictures = "/Users/joerg/repos/braz/site_pictures"
        path_to_site_picture = os.path.join(path_folder_site_pictures, name_tmp)

        self.site_pixmap = QPixmap(path_to_site_picture)
        scaled_site_picture = self.site_pixmap.scaled(self.label_for_site_picture.size() / 4, QtCore.Qt.KeepAspectRatio)
        picture_height = self.label_for_site_picture.height()
        self.braz_pic.setFixedWidth(picture_height)
        print('label_size: ', self.braz_pic.geometry())
        self.label_for_site_picture.setPixmap(scaled_site_picture)
        print('label_total: ', self.label_for_site_picture.width())
        # Fill the label_picture layout
        self.label_pic_and_site_pictures.addWidget(self.braz_pic)
        self.label_pic_and_site_pictures.addStretch()
        self.label_pic_and_site_pictures.addWidget(self.label_for_site_picture)

        # layout for QTableWidget AND search_btn_layout
        self.qtable_search_btn_layout = QHBoxLayout()

        # layout only for QTablewidget
        self.qtable_layout = QHBoxLayout()
        self.bra_dir_table = QTableWidget()
        print('width: ', self.bra_dir_table.width())
        # self.bra_dir_table.setGeometry(QtCore.QRect(0, 0, 1411, 161))
        self.bra_dir_table.setColumnCount(15)
        self.bra_dir_table.setHorizontalHeaderLabels(["Nr.", "Site", "PS1", "PS2", "PS3", "PS4",
                                                      "PS5", "PS6", "PS7", "PS8", "PS9", "PS10",
                                                      "title", "loc", "link"])
        # self.bra_dir_table.setColumnWidth(0, 25)
        # self.bra_dir_table.setColumnWidth(1, 80)
        # self.bra_dir_table.setColumnWidth(2, 80)

        header = self.bra_dir_table.horizontalHeader()
        #header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)

        self.qtable_layout.addWidget(self.bra_dir_table)

        # layout for the control_buttons on the right side
        self.search_btn_layout = QVBoxLayout()

        # Define layout for a horizontal line...
        self.hor_lin_1_layout = QHBoxLayout()
        self.hor_lin_1_layout.addWidget(QHLine())

        # Define layout for a horizontal line...
        self.hor_lin_2_layout = QHBoxLayout()
        self.hor_lin_2_layout.addWidget(QHLine())

        # Define layout for a horizontal line...
        self.hor_lin_3_layout = QHBoxLayout()
        self.hor_lin_3_layout.addWidget(QHLine())


        # first horizontal button row...
        self.first_horizontal_box = QHBoxLayout()
        self.sites_label = QLabel("Sites: ")
        self.comboBox_sites = QComboBox()
        self.first_horizontal_box.addWidget(self.sites_label)
        self.first_horizontal_box.addWidget(self.comboBox_sites)

        # first second button row...
        self.second_horizontal_box = QHBoxLayout()
        self.site_label_search = QLabel("Search for PS: ")
        self.site_label_search.setStyleSheet("font-size: 12px;" "color: green;")
        self.site_comboBox_search_ps = QComboBox()
        self.second_horizontal_box.addWidget(self.site_label_search)
        self.second_horizontal_box.addWidget(self.site_comboBox_search_ps)

        # first third button row...
        self.third_horizontal_box = QHBoxLayout()

        self.header_selected_ps = QLabel("Sites of the selected PS")
        self.header_selected_ps.setStyleSheet("font: Monaco;" "color: blue;")
        self.third_horizontal_box.addWidget(self.header_selected_ps)

        # Define layout for a horizontal line...
        self.hor_lin_4_layout = QHBoxLayout()
        self.hor_lin_4_layout.addWidget(QHLine())

        # first second button row...
        self.fourth_horizontal_box = QHBoxLayout()
        selected_ps_name = "Rebecca More"
        self.lbl_selected_ps = QLabel(selected_ps_name)
        self.lbl_selected_ps.setStyleSheet("font-size: 12px;" "color: green;")
        self.sites_of_selected_ps = QComboBox()
        for cnts in ['Milfs Like It Big', 'Big Tits In Uniform']:
            self.sites_of_selected_ps.addItem(cnts)
        self.fourth_horizontal_box.addWidget(self.lbl_selected_ps)
        self.fourth_horizontal_box.addWidget(self.sites_of_selected_ps)

        # Fill the vertical layout on the right side.
        self.search_btn_layout.addLayout(self.first_horizontal_box)
        self.search_btn_layout.addLayout(self.hor_lin_1_layout)
        self.search_btn_layout.addLayout(self.second_horizontal_box)
        self.search_btn_layout.addLayout(self.hor_lin_2_layout)
        self.search_btn_layout.addLayout(self.third_horizontal_box)
        self.search_btn_layout.addLayout(self.fourth_horizontal_box)
        self.search_btn_layout.addStretch()

        # FIll the QTableWidget_layout and search_btn_layout
        self.qtable_search_btn_layout.addLayout(self.qtable_layout)
        #self.qtable_search_btn_layout.addStretch()
        #self.qtable_search_btn_layout.insertStretch(0, 10)
        self.qtable_search_btn_layout.addLayout(self.search_btn_layout)
        #self.qtable_search_btn_layout.addStretch()

        # Arange the layout in the desired manner:
        self.complete_layout.addLayout(self.label_pic_and_site_pictures)
        #self.complete_layout.addStretch()
        self.complete_layout.addLayout(self.qtable_search_btn_layout)
        #elf.complete_layout.addStretch()

        # Set the hand-made complete layout in a superordinate QWidget called dummy_widget
        dummy_widget = QWidget()
        dummy_widget.setLayout(self.complete_layout)
        self.setCentralWidget(dummy_widget)

        # #############################################
        #  End of definition of the layout
        # #############################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowBrazzers()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())