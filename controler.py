from views.view1 import ATM

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

class Controller():
    def __init__(self, master, bank_db):

        self.master = master
        self.bank_db = bank_db
        self.bank_gui = ATM(master)
        self.bank_db.read_file()
        self.accNum = 0
        self.bank_gui.loginBut.config(command= self.Login)


        # self.bank_gui.new_entry.bind("<Return>", self._add)
        # self.bank_gui.add_button.config(command=self._add)

    def Login(self):
        self.accNum = self.bank_gui.uentry.get()
        pin = self.bank_gui.passInp.get()
        if self.accNum in self.bank_db.accounts:
            if pin == self.bank_db.accounts[self.accNum]['PIN']:
                self.gotoMain()
                self.bank_db.makeNew(self.accNum, int(self.bank_db.accounts[self.accNum]['Balance']))
            else:
                print('wrong pin')
        else:
            print('no user')

    def gotoDep(self):
        self.bank_gui.Deposit()
        self.bank_gui.submitButton.config(command=self.Deposit)
        self.bank_gui.backBut.config(command=self.gotoMain)

    def gotoMain(self):
        self.bank_gui.MainMenu()
        self.bank_gui.depositBut.config(command=self.gotoDep)
        self.bank_gui.withdrawBut.config(command=self.gotoWith)


    def gotoWith(self):
        self.bank_gui.Withdraw()
        self.bank_gui.backBut.config(command=self.gotoMain)
        self.bank_gui.WBut20.config(command=self.do20)
        self.bank_gui.WBut40.config(command=self.do40)
        self.bank_gui.WBut60.config(command=self.do60)
        self.bank_gui.WBut80.config(command=self.do80)
        self.bank_gui.WBut100.config(command=self.do100)
        self.bank_gui.WBut150.config(command=self.do150)
        self.bank_gui.WBut200.config(command=self.do200)
        self.bank_gui.WButChoice.config(command=self.doCoice)

    def do20(self):
        self.Withdraw(20)

    def do40(self):
        self.Withdraw(40)

    def do60(self):
        self.Withdraw(60)

    def do80(self):
        self.Withdraw(80)

    def do100(self):
        self.Withdraw(100)

    def do150(self):
        self.Withdraw(150)

    def do200(self):
        self.Withdraw(200)

    def doCoice(self):
        self.bank_gui.Coice()

    def save(self):
        self.bank_db.write_file()

    def Deposit(self):
        try:
            money = int(self.bank_gui.money_box.get())
            self.bank_db.user.deposit(money)
            print(type(self.bank_db.accounts[self.accNum]['Balance']))
            self.bank_db.accounts[self.accNum]['Balance'] += money
            self.save()
        except ValueError:
            print('plese enter a number')

    def Withdraw(self, amount):
        print(amount)




