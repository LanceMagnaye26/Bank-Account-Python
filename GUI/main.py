from tkinter import *
from GUI.controller import Controller
from GUI.model import Model


def main():
    root = Tk()
    root.title("Sign In")
    icon = PhotoImage(file="icon.png")
    root.tk.call("wm", 'iconphoto', root._w, icon)
    name_db = Model()
    Controller(root, name_db)
    mainloop()

if __name__ == "__main__":
    main()