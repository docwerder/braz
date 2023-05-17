from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from qt_material import apply_stylesheet

app = QApplication()

# qt_material anwenden
apply_stylesheet(app, theme='my_theme.xml')

# QTableWidget erstellen und Eigenschaften anpassen
table_widget = QTableWidget()
table_widget.setRowCount(2)
table_widget.setColumnCount(3)

for row in range(table_widget.rowCount()):
    for column in range(table_widget.columnCount()):
        item = QTableWidgetItem()
        # item.setTextAlignment(Qt.AlignCenter)
        item.setText(f"Zelle {row}, {column}")
        # Hintergrundfarbe
        palette = app.palette()
        background_color = QColor(palette.color(QPalette.Dark))
        item.setBackground(background_color)
        table_widget.setItem(row, column, item)

table_widget.show()
app.exec_()
