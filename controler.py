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
        self.accNum = 0
        self.name_gui.loginBut.config(command= self.Login)


        # self.name_gui.new_entry.bind("<Return>", self._add)
        # self.name_gui.add_button.config(command=self._add)

    def Login(self):
        self.accNum = self.name_gui.uentry.get()
        pin = self.name_gui.passInp.get()
        if self.accNum in self.name_db.accounts:
            if pin == self.name_db.accounts[self.accNum]['PIN']:
                self.name_gui.MainMenu()
                self.name_gui.depositBut.config(command=self.addDep)
            else:
                print('wrong pin')
        else:
            print('no user')

    def addDep(self):
        self.name_gui.Deposit()
        self.name_gui.submitButton.config(command=self.Deposit)


    def Deposit(self):
        money = self.name_gui.money_box.get()
        print(money)





