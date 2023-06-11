import PyQt5.QtWidgets as widget
import PyQt5.QtGui as interface
from PyQt5.QtCore import *


class Mainwindow(widget.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window Title')
        self.setWindowIcon(interface.QIcon('0001.jpg'))
        self.setLayout(widget.QVBoxLayout())

        frame = widget.QFrame(self)
        self.layout().addWidget(frame)

        label = widget.QLabel("Hello world, what's your name")
        self.layout().addWidget(label)
        # label.setAlignment(Qt.AlignCenter)

        entry = widget.QLineEdit(frame)
        self.layout().addWidget(entry)

        self.show()


app = widget.QApplication([])
win = Mainwindow()

app.exec_()