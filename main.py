from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


app = QApplication([])
widget = QWidget()
widget.setWindowTitle("Company")
btn = QPushButton('push')
layout = QVBoxLayout(widget)
layout.addWidget(btn)
widget.show()
app.exec_()
