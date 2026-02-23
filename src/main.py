import pyautogui
import tkinter as tk
from pynput import keyboard
import threading

class Gui:
    def __init__(self):
        self.root = tk.Tk()

        self.repeating_key = ""
        self.root.geometry("300x300")
        self.root.title("AutoKey")

        self.root.repeat_key_button = tk.Button(self.root, text="Change Repeat Key",command=self.repeat_key_button_click)
        self.root.repeat_key_button.pack()

        self.root.start_repeating_button = tk.Button(self.root, text="balls", command=self.start_repeating)
        self.root.start_repeating_button.pack()

        self.root.mainloop()

    def start_repeating(self):
        while True:
            pyautogui.write(self.repeating_key, interval=0.25)

    def repeat_key_button_click(self):
        repeat_root = tk.Toplevel(self.root)
        repeat_root.geometry("300x300")
        repeat_root.title("Repeat key Changer")

        repeat_entry = tk.Entry(repeat_root)
        repeat_entry.pack()

        def get_button():
            self.repeating_key = repeat_entry.get()

        entry_get_button = tk.Button(repeat_root, text="Change Repeat Key", command=get_button)
        entry_get_button.pack()


def main():
    def on_press(key):
        try:
            if key.char == "8":
                print("hthjet")
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    listener = keyboard.Listener(
        on_press=on_press,
    )

    listener.start()
    listener.join()


test = Gui()
threading.Thread(target=main).start()

#pyautogui.write('Hello world!')
#pyautogui.write('Hello world!', interval=0.25)
