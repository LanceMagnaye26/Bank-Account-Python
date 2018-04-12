import json
#pin in different file
#chequing and savings account
#transaction log
#transaction teller
#delete account give money
#receipt
#confirm pin
#managing accounts

class Model():

    _NEXT_ACC_NUM = 1000000

    def __init__(self):
        self.filename = 'accounts.json'
        self.accounts = {}

    def write_file(self):
        with open(self.filename, 'w') as open_f:
            json.dump(self.accounts, open_f)

    def read_file(self):
        try:
            with open(self.filename, 'r') as open_f:
                self.accounts = {}
                self.accounts = json.load(open_f)
        except FileNotFoundError:
            self.write_file()


    def add_account(self, f_name, l_name, pin):
        self.read_file()
        n = 0
        for user in self.accounts:
            if n < int(user):
                n = int(user)
        acc_num = n + 1
        self.accounts[acc_num] = {'PIN': pin, 'First Name': f_name, 'Last Name': l_name, 'Type': {'Chequing': {'Balance': 0, 'Transaction Log': []}, 'Savings': {'Balance':0, 'Transaction Log': []}}}
        self.write_file()

    def del_account(self, acc_num):
        self.read_file()
        del self.accounts[str(acc_num)]
        self.write_file()

    def pin_check(self, acc_num, pin):
        self.read_file()
        if pin == self.accounts[acc_num]['PIN']:
            return True

    def no_user_check(self, acc_num):
        self.read_file()
        if str(acc_num) in self.accounts:
            return True

if __name__ == '__main__':
    m = Model()
    m.del_account(1)
    # print(m.accounts)
    # print(m.accounts)