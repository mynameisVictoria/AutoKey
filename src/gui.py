import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout,QComboBox,QLabel
from PyQt5.QtCore import Qt
import sys
import time
from pynput.keyboard import Controller
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

        self.error_label = QLabel("Error label")
        combo_layout.addWidget(self.error_label)
        self.info_label = QLabel(f"Repeating: {self.repeat_value}, Pause: {self.stop_value}, Tick: {self.interval}\nClick your pause key to begin")
        combo_layout.addWidget(self.info_label)

        main_layout.addLayout(row_layout)
        main_layout.addLayout(combo_layout)

    def button_clicked(self):
        if self.dropdown.currentText() == "Repeat Key":
            if len(self.input_field.text()) == 1:
                self.repeat_value = self.input_field.text()
                self.error_label.setText("Error label")
            else:
                self.error_label.setText("Must be 1 letter")

        elif self.dropdown.currentText() == "Stop/Pause key":
            if len(self.input_field.text()) == 1:
                self.error_label.setText("Error label")
                self.stop_value = self.input_field.text()
            else:
                self.error_label.setText("Must be 1 letter")

        elif self.dropdown.currentText() == "Tick Interval":
            try:
                interval = float(self.input_field.text())
                if interval <= 0:
                    self.error_label.setText("Must positive value")
                else:
                    self.interval = interval
                    self.error_label.setText("Error label")
            except ValueError:
                self.error_label.setText("Must be an integer/decimal value")

        self.info_label.setText(f"Repeating: {self.repeat_value}, Pause: {self.stop_value}, Tick: {self.interval}\nClick your pause key to begin")

    def repeat(self):
        while True:
            if self.pause_value:
                time.sleep(self.interval)
                self.keycon.press(f"{self.repeat_value}")
            else:
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    def on_press(key):
        if str(format(key)).lower() == "'" + window.stop_value.lower() + "'":
            if window.pause_value:
                window.pause_value = False
            else:
                window.pause_value = True
                threading.Thread(target=window.repeat).start()

    listener = keyboard.Listener(
        on_press=on_press, )

    listener.start()

    app.aboutToQuit.connect(listener.stop)
    sys.exit(app.exec_())