from PySide2.QtCore import Qt
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QComboBox, QMainWindow, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-Select Combo Box Example")

        combo_box = QComboBox(self)
        combo_box.view().setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        combo_box.setModel(QStandardItemModel())
        combo_box.setInsertPolicy(QComboBox.InsertAtBottom)
        combo_box.setEditable(True)
        combo_box.lineEdit().setReadOnly(True)
        combo_box.lineEdit().setAlignment(Qt.AlignCenter)

        for i in range(5):
            item = QStandardItem(f"Item {i}")
            item.setCheckable(True)
            combo_box.model().appendRow(item)

        self.setCentralWidget(combo_box)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()