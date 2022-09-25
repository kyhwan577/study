from PySide2.QtWidgets import QApplication, QWidget


app = QApplication([])
widget = QWidget()
widget.setWindowTitle("Company")
widget.show()

app.exec_()