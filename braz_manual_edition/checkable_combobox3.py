from PySide2.QtCore import Qt
from PySide2.QtGui import QStandardItemModel, QStandardItem 
from PySide2.QtWidgets import QApplication, QCheckBox, QComboBox, QMainWindow, QVBoxLayout, QWidget, QAbstractItemView

class CheckableComboBox(QComboBox):
    def __init__(self):
        super().__init__()

        self.view().pressed.connect(self.handle_item_pressed)
        self.view().setSelectionMode(QAbstractItemView.NoSelection.NoSelection)
        self.setModel(QStandardItemModel(self))

    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if not item.isEnabled():
            return

        item.setCheckState(Qt.Checked if item.checkState() == Qt.Unchecked else Qt.Unchecked)
        values = [self.model().item(i).text() for i in range(self.model().rowCount()) if self.model().item(i).checkState() == Qt.Checked]
        self.setEditText(", ".join(values))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-Select Combo Box Example")

        combo_box = CheckableComboBox()

        for i in range(5):
            item = QStandardItem(f"Item {i}")
            item.setCheckable(True)
            item.setEditable(False)
            item.setSelectable(True)
            item.setCheckState(Qt.Unchecked)
            combo_box.model().appendRow(item)

            checkbox = QCheckBox()
            checkbox.setChecked(False)
            checkbox.stateChanged.connect(lambda state, item=item: item.setCheckState(state))
            combo_box.view().setIndexWidget(item.index(), checkbox)

        self.setCentralWidget(combo_box)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()