from PySide2 import QtWidgets, QtGui, QtCore

class ColorDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(ColorDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        value = index.data(QtCore.Qt.DisplayRole)  # Wert der Zelle abrufen
        color = None

        # Beispielkriterium: Wenn der Wert größer als 5 ist, wird die Schriftfarbe rot
        if value > 5:
            color = QtGui.QColor("red")

        # Standardrendervorgang ausführen
        option.palette.setColor(QtGui.QPalette.Text, color)
        super(ColorDelegate, self).paint(painter, option, index)

app = QtWidgets.QApplication([])

table = QtWidgets.QTableWidget(4, 2)
delegate = ColorDelegate()
table.setItemDelegate(delegate)

# Beispielwerte setzen
table.setItem(0, 0, QtWidgets.QTableWidgetItem("Wert 1"))
table.setItem(0, 1, QtWidgets.QTableWidgetItem("7"))
table.setItem(1, 0, QtWidgets.QTableWidgetItem("Wert 2"))
table.setItem(1, 1, QtWidgets.QTableWidgetItem("3"))
table.setItem(2, 0, QtWidgets.QTableWidgetItem("Wert 3"))
table.setItem(2, 1, QtWidgets.QTableWidgetItem("9"))
table.setItem(3, 0, QtWidgets.QTableWidgetItem("Wert 4"))
table.setItem(3, 1, QtWidgets.QTableWidgetItem("2"))

table.show()
app.exec_()
