from models.account import Account
import os
from os import path
import csv



class Model():
    def __init__(self):
        super().__init__()
        self.accounts = {}

    def read_file(self):
        try:
            with open('CLI/accounts.csv', 'r') as open_f:
                csv_reader = csv.DictReader(open_f)
                for user in csv_reader:
                    self.accounts[user['Account Number']] = {'First Name': user['First Name'], 'Last Name': user['Last Name'], 'PIN': user['PIN']}

            #print(self.accounts)
        except FileNotFoundError:
            self.write_file()

    def write_file(self):
        pass

    def makeNew(self , name):

        user = Account(name)
        print(user)



