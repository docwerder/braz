from PySide2.QtWidgets import QApplication, QComboBox, QMainWindow, QSizePolicy, QAbstractItemView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-Select Combo Box Example")

        combo_box = QComboBox(self)
        combo_box.view().setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        combo_box.view().setSelectionMode(QAbstractItemView.ExtendedSelection)
        combo_box.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

        self.setCentralWidget(combo_box)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()