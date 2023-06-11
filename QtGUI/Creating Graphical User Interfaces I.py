import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # -------------------------------------Add Title (self.)
        self.setWindowTitle("Hello World")

        # ----------------------------------Set Vertical Layout (self.)
        self.setLayout(qtw.QVBoxLayout())   # for horizontal layout: self.setLayout(qtw.QHBoxLayout())

        # ---------------------------------------------------------Add Label (QLabel)
        my_label = qtw.QLabel("Hello World! What's your name")

        # Change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))

        # Set Layout for label
        self.layout().addWidget(my_label)

        # ----------------------------------Add Entry Box (QLineEdit)
        my_entry = qtw.QLineEdit()

        # Create object name to reference the entry box later
        my_entry.setObjectName("name_field")

        # Set placeholder text
        my_entry.setText("")

        # Set Layout for entry box (QLineEdit) to add to screen
        self.layout().addWidget(my_entry)

        # ------------------------------------------Create button (QPushButton)
        my_button = qtw.QPushButton("Click Me",clicked= lambda: press_it())

        # Set layout for button
        self.layout().addWidget(my_button)

        # Show the App
        self.show()

        def press_it():

            # Add name to label
            my_label.setText(f'Hello {my_entry.text()}!')   # f string to replace label with user input

            # Clear Entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
