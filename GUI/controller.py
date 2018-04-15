from view import ATM
from time import gmtime, strftime

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

class Controller():
    def __init__(self, master, bank_db):
        self.master = master
        self.bank_db = bank_db
        self.bank_db.read_file()
        self.bank_gui = ATM(master)
        self.accNum = 0
        self.gotoLogin()

        # self.bank_gui.new_entry.bind("<Return>", self._add)
        # self.bank_gui.add_button.config(command=self._add)

    def Login(self):
        self.accNum = self.bank_gui.uentry.get()
        if self.accNum in self.bank_db.accounts:
            self.gotoPass()
        else:
            messagebox.showinfo("Error", "Error: no user!")

    def Password(self):
        try:
            pin = int(self.bank_gui.passInp.get())
            passwd = int(self.bank_db.accounts[self.accNum]["PIN"]) / int(self.bank_db.accounts[self.accNum]["key"])
            if pin == passwd:
                self.gotoAcounts()
                self.user = self.bank_db.accounts[self.accNum]
            else:
                messagebox.showinfo("Pin", 'wrong pin')
        except:
            messagebox.showinfo("Wrong pin", "Pin must be 4 or 6 digits and a number")

    def Deposit(self):
        try:
            money = float(self.bank_gui.money_box.get())
            self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] += money
            self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append('Deposited ${} on {}'.format(money, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
            self.gotoFinish('Deposited ${} into {}'.format(money, self.accType))
        except ValueError:
            messagebox.showinfo("Error", "Error: please enter a number")

    def Withdraw(self, amount):
        try:
            amount = float(amount)
            if self.accType == 'Chequing':
                if self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] - amount > -500:
                    self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] -= amount
                    self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append(
                        'Withdrew ${} on {}'.format(amount, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                    self.gotoFinish('Withdrew ${} from {}'.format(amount, self.accType))
                else:
                    messagebox.showinfo("Error", 'not enough funds')
            else:
                if self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] < amount:
                    messagebox.showinfo("Error",'not enough funds')
                elif self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] - amount < 1000:
                    messagebox.showinfo("Error",'funds bellow 1000, $10 fee charges')
                    self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] -= amount + 10
                    self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append(
                        'Withdrew ${} on {}'.format(amount, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                    self.gotoFinish('Withdrew ${} from Savings on {}, $10 fee was charged'.format(amount, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                else:
                    self.bank_db.accounts[self.accNum]['Type'][self.accType]['Balance'] -= amount
                    self.bank_db.accounts[self.accNum]['Type'][self.accType]['Transaction Log'].append(
                        'Withdrew ${} on {}'.format(amount, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
                    self.gotoFinish('Withdrew ${} from Savings'.format(amount))
        except ValueError:
            messagebox.showinfo("Error", "Error: please enter a number")

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
