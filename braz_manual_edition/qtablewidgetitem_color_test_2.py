from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

app = QApplication()

# Laden der Farben aus der dark_amber.xml-Datei in ein QPalette-Objekt
palette = QPalette()
palette_file = open('/Users/joerg/opt/anaconda3/envs/pyside2_dev/lib/python3.10/site-packages/qt_material/themes/my_dark_amber.xm')
palette.read(palette_file)

# Erstellung des QTableWidget
table = QTableWidget()
table.setRowCount(3)
table.setColumnCount(3)

# Setzen der Hintergrundfarbe und Schriftfarbe einer Zelle im QTableWidget
row = 1
column = 1
item = QTableWidgetItem('Test')
item.setBackground(QColor(palette.color(QPalette.Background)))
item.setForeground(QColor(palette.color(QPalette.Text)))
table.setItem(row, column, item)

table.show()
app.exec_()
