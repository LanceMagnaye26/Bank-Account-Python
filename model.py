from models.account import Account
import os
from os import path



class Model():
    def __init__(self):
        super().__init__()
        self.filename = ''


    def makeNew(self , name):

        user = Account(name)
        print(user)



