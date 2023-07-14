import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def set_dark_mode(self):
        app.setStyle(QStyleFactory.create("Fusion"))
        palette = self.palette()
        palette.setColor(palette.Window, QColor(53, 53, 53))
        palette.setColor(palette.WindowText, Qt.white)
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.set_dark_mode()
    mainWindow.show()
    sys.exit(app.exec_())
