from account import Account
import os
from os import path
import json



class Model():
    def __init__(self):
        #super().__init__()
        self.accounts = {}
        cwd = os.getcwd()
        cwd = cwd.split('\\')
        new_cwd = ''
        for item in cwd:
            if item != 'GUI':
                new_cwd += item
                new_cwd += '\\'
        self.filename = new_cwd+'\\CLI\\accounts.json'

    def makeNew(self , name, bal):
        self.user = Account(name, bal)

    def write_file(self):
        with open(self.filename, 'w') as open_f:
            json.dump(self.accounts, open_f)

    def read_file(self):
        try:
            with open(self.filename, 'r') as open_f:
                self.accounts = {}
                self.accounts = json.load(open_f)
        except FileNotFoundError:
            print('Please create an account via CLI/main.py')
            self.write_file()




