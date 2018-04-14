from models.account import Account
import os
from os import path
import json



class Model():
    def __init__(self):
        #super().__init__()
        self.fieldnames = ['First Name', 'Last Name', 'Account Number', 'PIN', 'Balance']
        self.accounts = {}

    def makeNew(self , name, bal):
        self.user = Account(name, bal)

    def write_file(self):
        with open('CLI/accounts.json', 'w') as open_f:
            json.dump(self.accounts, open_f)

    def read_file(self):
        try:
            with open('CLI/accounts.json', 'r') as open_f:
                self.accounts = {}
                self.accounts = json.load(open_f)
        except FileNotFoundError:
            self.write_file()




