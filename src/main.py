import os
import threading
from pynput.keyboard import Key, Controller
from pynput import keyboard
import time


class Establish:
    def __init__(self):
        self.break_key = ""
        self.repeat_key = ""
        self.interval = 1
        self.keycon = Controller()

    def establish(self):
        while True:
            self.repeat_key = input("What key would you wish to repeat?")
            if len(self.repeat_key) == 1:
                break
            else:
                print("Please enter a single character")
        while True:
            self.break_key = input("What key would you wish to break?")
            if len(self.break_key) == 1:
                break
            else:
                print("Please enter a single character")
        while True:
            self.interval = float(input("How many seconds would you like to wait between each repeat?"))
            if self.interval >0:
                break
            else:
                print("Please enter a valid interval")

        self.repeat()

    def repeat(self):
        while True:
            time.sleep(self.interval)
            self.keycon.press(f"{self.repeat_key}")


def on_press(key):
    print("\n\n",key, obj.break_key,"\n\n")
    if str(format(key)).lower() == "'" + obj.break_key.lower() + "'":
        os._exit(0)

listener = keyboard.Listener(
    on_press=on_press,
)


obj = Establish()
est_thread = threading.Thread(target=obj.establish)
est_thread.start()

listener.start()
listener.join()




