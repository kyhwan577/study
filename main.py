from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


app = QApplication([])
widget = QWidget()
widget.setWindowTitle("Company")
label = QLabel("Add")
layout = QVBoxLayout(widget)
layout.addWidget(label)
widget.show()

app.exec_()
