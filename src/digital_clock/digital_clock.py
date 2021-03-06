from tkinter import Checkbutton, StringVar, Tk, mainloop, messagebox
from time import strftime
from tkinter.ttk import Button, Label
import webbrowser
import requests
from __init__ import __version__ as version

root = Tk()
root.title("Digital Clock")
root.resizable(False, False)
root.attributes("-topmost", True)

agreement = StringVar()

url = f"https://github.com/Nukecraft5419/DigitalClock/releases/latest"
response = requests.get(url, verify=False, timeout=5)
repo_version = response.url.split('/')[-1]
version = version


def time():  # Digital Clock System
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


def clicked():
    webbrowser.open(url)


def agreement_changed():
    if (agreement.get() == "agree"):
        root.attributes("-topmost", True)
        root.update()
    else:
        root.attributes("-topmost", False)
        root.update()


if (repo_version != version):
    messagebox.showinfo("Update", "There is a new version of DigitalClock!")
    Label(root, text="There is a new version of DigitalClock!").pack()
    Button(root, text="Update", command=clicked).pack()


# Label Style
label = Label(root, font=("Helvetica", 80),
              background="#fefae0", foreground="#d4a373")
label.pack(anchor="center")

Checkbutton(root, text="Top window", command=agreement_changed,
            variable=agreement, onvalue="agree", offvalue="disagree").pack()

time()
mainloop()
