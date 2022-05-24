from tkinter import Tk, mainloop
from time import strftime
from tkinter.ttk import Label

root = Tk()
root.title("Digital Clock")
root.resizable(False, False)

def raise_above_all():
    root.attributes('-topmost', True)
    window.update()
    window.attributes('-topmost', False)

def time():  # Digital Clock System
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


# Label Style
label = Label(root, font=("Helvetica", 80),
              background="#fefae0", foreground="#d4a373")
label.pack(anchor="center")

time()
mainloop()
