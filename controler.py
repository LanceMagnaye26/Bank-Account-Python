from views.view1 import ATM

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

class Controller():
    def __init__(self, master, name_db):

        self.master = master
        self.name_db = name_db
        self.name_gui = ATM(master)
        self.name_db.read_file()

        self.name_gui.loginBut.config(command= self.Login)

        # self.name_gui.new_entry.bind("<Return>", self._add)
        # self.name_gui.add_button.config(command=self._add)

    def Login(self):
        name = self.name_gui.uentry.get()
        self.name_gui.MainMenu()
        self.name_db.makeNew(name)





