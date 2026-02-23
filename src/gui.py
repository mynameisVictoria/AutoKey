from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout,QComboBox,QLabel
from PyQt5.QtCore import Qt
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.interval = 1
        self.repeat_value = "A"
        self.stop_value = "B"

        self.setFixedSize(250,200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        row_layout = QHBoxLayout()


        #--------------------------------------# the main input field and buttons
        confirm_button = QPushButton("Confirm")
        confirm_button.setFixedSize(50, 50)
        row_layout.addWidget(confirm_button, alignment=Qt.AlignBottom)

        self.input_field = QLineEdit()
        self.input_field.setFixedSize(180,50)
        row_layout.addWidget(self.input_field, alignment=Qt.AlignBottom)
        #--------------------------------------#
        combo_layout = QVBoxLayout()

        self.dropdown = QComboBox()
        self.dropdown.addItems(["Option 1", "Option 2", "Option 3"])
        combo_layout.addWidget(self.dropdown)

        self.label = QLabel("Hello, world!")
        combo_layout.addWidget(self.label)

        main_layout.addLayout(row_layout)
        main_layout.addLayout(combo_layout)

    def repeat(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())