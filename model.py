from models.account import Account
import os
from os import path
import csv



class Model():
    def __init__(self):
        super().__init__()
        self.fieldnames = ['First Name', 'Last Name', 'Account Number', 'PIN', 'Balance']
        self.accounts = {}

    def read_file(self):
        try:
            with open('CLI/accounts.csv', 'r') as open_f:
                csv_reader = csv.DictReader(open_f)
                for user in csv_reader:
                    self.accounts[user['Account Number']] = {'First Name': user['First Name'], 'Last Name': user['Last Name'], 'PIN': user['PIN'], 'Balance':int(user['Balance'])}

            #print(self.accounts)
        except FileNotFoundError:
            self.write_file()

    def write_file(self):
        with open('CLI/accounts.csv', 'w') as open_f:
            csv_writer = csv.DictWriter(open_f, fieldnames=self.fieldnames, delimiter=',')
            csv_writer.writeheader()
            for user, value in self.accounts.items():
                dict = {'Account Number': user,
                        'First Name': value['First Name'],
                        'Last Name': value['Last Name'],
                        'PIN': value['PIN'],
                        'Balance': value['Balance']
                }
                csv_writer.writerow(dict)

    def makeNew(self , name, bal):
        self.user = Account(name, bal)




