import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout,QComboBox,QLabel
from PyQt5.QtCore import Qt
import sys
import time
from pynput.keyboard import Key, Controller
from pynput import keyboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.keycon = Controller()
        self.pause_value = False
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
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setFixedSize(50, 50)
        self.confirm_button.clicked.connect(self.button_clicked)
        row_layout.addWidget(self.confirm_button, alignment=Qt.AlignBottom)

        self.input_field = QLineEdit()
        self.input_field.setFixedSize(180,50)
        row_layout.addWidget(self.input_field, alignment=Qt.AlignBottom)
        #--------------------------------------#
        combo_layout = QVBoxLayout()

        self.dropdown = QComboBox()
        self.dropdown.addItems(["Repeat Key", "Stop/Pause key", "Tick Interval"])
        combo_layout.addWidget(self.dropdown)

        self.label = QLabel("Hello, world!")
        combo_layout.addWidget(self.label)

        main_layout.addLayout(row_layout)
        main_layout.addLayout(combo_layout)

    def button_clicked(self):
        if self.dropdown.currentText() == "Repeat Key":
            if len(self.input_field.text()) == 1:
                self.repeat_value = self.input_field.text()
                self.label.setText("Error label")
            else:
                self.label.setText("Must be 1 letter")

        elif self.dropdown.currentText() == "Stop/Pause key":
            if len(self.input_field.text()) == 1:
                self.label.setText("Error label")
                self.stop_value = self.input_field.text()
            else:
                self.label.setText("Must be 1 letter")

        elif self.dropdown.currentText() == "Tick Interval":
            try:
                interval = float(self.input_field.text())
                self.interval = interval
                self.label.setText("Error label")
            except ValueError:
                self.label.setText("Must be an integer/decimal value")

    def repeat(self):
        while True:
            if self.pause_value:
                time.sleep(self.interval)
                self.keycon.press(f"{self.repeat_value}")
            else:
                print(window.pause_value, "IM HERE 4")
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    def on_press(key):
        if str(format(key)).lower() == "'" + window.stop_value.lower() + "'":
            print(window.pause_value, "IM HERE 3")
            if window.pause_value:
                window.pause_value = False
                print(window.pause_value, "IM HERE 1")
            else:
                window.pause_value = True
                print(window.pause_value, "IM HERE 2")
                thread = threading.Thread(target=window.repeat).start()
                print("IM HERE 5")

    listener = keyboard.Listener(
        on_press=on_press, )

    listener.start()

    app.aboutToQuit.connect(listener.stop)
    sys.exit(app.exec_())