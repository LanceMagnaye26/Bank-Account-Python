from views.view1 import ATM

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

class Controller():
    def __init__(self, master, bank_db):
        self.TABLE = "6,9,7,0,3,2,4,5,1,8,6,9"
        self.master = master
        self.bank_db = bank_db
        self.bank_gui = ATM(master)
        self.bank_db.read_file()
        self.accNum = 0
        self.gotoLogin()

        # self.bank_gui.new_entry.bind("<Return>", self._add)
        # self.bank_gui.add_button.config(command=self._add)

    def Login(self):
        self.accNum = self.bank_gui.uentry.get()
        if self.accNum in self.bank_db.accounts:
            self.gotoPass()
        else:
            messagebox.showinfo("Error",'no user')

    def Password(self):
        try:

            pin = int(self.bank_gui.passInp.get())
            answer = ""
            stringed = str(pin)
            while len(stringed) > 0:
                for pos in range(len(self.TABLE)):
                    if self.TABLE[pos] == stringed[-1]:
                        equiv = str(self.TABLE[pos + 2])
                answer = answer + equiv
                stringed = stringed[:-1]
            if answer == self.bank_db.accounts[self.accNum]['PIN']:
                self.gotoAcounts()
                self.user = self.bank_db.accounts[self.accNum]
            else:
                messagebox.showinfo("Pin", 'wrong pin')
        except:
            messagebox.showinfo("Pin", "Pin must be 4 digits and a number")

    def Deposit(self):
        try:
            money = int(self.bank_gui.money_box.get())
            self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] += money
            self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append('Deposited {}'.format(money))
            self.gotoFinish('Deposited {} into {}'.format(money, self.accType))
        except ValueError:
            messagebox.showinfo("Error",'plese enter a number')

    def Withdraw(self, amount):
        #can go up to -500
        if self.accType == 'Chequing':
            if self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] - amount > -500:
                self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] -= amount
                self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append(
                    'Deposited {}'.format(amount))
                self.gotoFinish('Withdrew {} from {}'.format(amount, self.accType))
        #can go down to 0
        #withdrawing below 1000 gives 10$ fee
        else:
            if self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] < amount:
                messagebox.showinfo("Error",'not enough funds')
            elif self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] - amount < 1000:
                messagebox.showinfo("Error",'funds bellow 1000, $10 fee charges')
                self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] -= amount + 10
                self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append(
                    'Withdrew {}'.format(amount))
                self.gotoFinish('Withdrew {} from Savings, $10 fee was charged'.format(amount))
            else:
                self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] -= amount
                self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append(
                    'Withdrew {}'.format(amount))
                self.gotoFinish('Withdrew {} from Savings'.format(amount))

    def Savings(self):
        self.accType = 'Savings'
        self.gotoMain()

    def Chequing(self):
        self.accType = 'Chequing'
        self.gotoMain()

    def Choice(self):
        try:
            money = int(self.bank_gui.money_box.get())
            self.Withdraw(money)
        except:
            messagebox.showinfo("Error",'plese enter a number')

    def gotoAcounts(self):
        self.bank_gui.SelectAcount()
        self.bank_gui.quitBut.config(command=self.gotoLogin)
        self.bank_gui.savingsBut.config(command=self.Savings)
        self.bank_gui.chequingBut.config(command=self.Chequing)

    def gotoPass(self):
        self.bank_gui.Password()
        self.bank_gui.loginBut.config(command=self.Password)
        self.bank_gui.quitBut.config(command=self.gotoLogin)

    def gotoLogin(self):
        self.bank_gui.Login()
        self.bank_gui.loginBut.config(command=self.Login)

    def gotoDep(self):
        self.bank_gui.Deposit()
        self.bank_gui.submitButton.config(command=self.Deposit)
        self.bank_gui.backBut.config(command=self.gotoMain)
        self.bank_gui.quitBut.config(command=self.gotoLogin)

    def gotoLogs(self):
        userlogs = self.bank_db.accounts[self.accNum]['Type'][self.accType]["Transaction Log"]
        string = ''
        while len(userlogs) > 20:
            userlogs.pop(0)
        for log in userlogs:
            string = string + '\n' + log
        if string == '':
            string = 'no transactions have been made'
        self.bank_gui.Logs(string)
        self.bank_gui.quitBut.config(command=self.gotoLogin)
        self.bank_gui.backBut.config(command=self.gotoAcounts)

    def gotoDetails(self):
        user = self.bank_db.accounts[self.accNum]
        string = 'Name: {}{} \nBalance: {}'.format(user['First Name'], user['Last Name'], user['Type'][self.accType]["Balance"])
        self.bank_gui.Details(string)
        self.bank_gui.quitBut.config(command=self.gotoLogin)
        self.bank_gui.backBut.config(command=self.gotoAcounts)

    def gotoMain(self):
        self.bank_gui.MainMenu()
        self.bank_gui.quitBut.config(command=self.gotoLogin)
        self.bank_gui.depositBut.config(command=self.gotoDep)
        self.bank_gui.withdrawBut.config(command=self.gotoWith)
        self.bank_gui.logBut.config(command=self.gotoLogs)
        self.bank_gui.detailBut.config(command=self.gotoDetails)

    def gotoWith(self):
        self.bank_gui.Withdraw()
        self.bank_gui.backBut.config(command=self.gotoAcounts)
        self.bank_gui.quitBut.config(command=self.gotoLogin)
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
        self.bank_gui.WithdrawOther()
        self.bank_gui.quitBut.config(command=self.gotoLogin)
        self.bank_gui.backBut.config(command=self.gotoAcounts)
        self.bank_gui.submitBut.config(command=self.Choice)

    def gotoFinish(self, message):
        self.save()
        self.bank_gui.Confirm(message)
        self.bank_gui.continueBut.config(command=self.gotoAcounts)
        self.bank_gui.quitBut.config(command=self.gotoLogin)

    def save(self):
        self.bank_db.write_file()
