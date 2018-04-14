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
    _TABLE = "6,9,7,0,3,2,4,5,1,8"

    def __init__(self):
        self.filename = 'accounts.json'
        self.accounts = {}
        self.tellers = {}


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

    def read_tellers_file(self):
        with open('tellers.json', 'r') as open_f:
            self.tellers = json.load(open_f)


    def add_account(self, f_name, l_name, pin):
        self.read_file()
        n = 0
        for user in self.accounts:
            if n < int(user):
                n = int(user)
        acc_num = n + 1
        self.accounts[acc_num] = {'PIN': self._encrypt(pin), 'First Name': f_name, 'Last Name': l_name, 'Type': {'Chequing': {'Balance': 0, 'Transaction Log': []}, 'Savings': {'Balance':0, 'Transaction Log': []}}}
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

    def no_teller_check(self, teller):
        self.read_tellers_file()
        if teller in self.tellers:
            return True

    def teller_password_check(self, teller, password):
        self.read_tellers_file()
        if str(password) == str(self.tellers[teller]['Password']):
            return True

    def pin_value_check(self, pin):
        try:
            pin = int(pin)
        except ValueError:
            return False

    def check_length(self, expected_length, actual_length):
        if actual_length == expected_length:
            return True

    def _encrypt(self, password):
        answer = ""
        stringed = str(password)
        while len(stringed) > 0:
            for pos in range(len(self._TABLE)):
                if self._TABLE[pos] == stringed[-1]:
                    equiv = str(self._TABLE[pos+2])
            answer = answer + equiv
            stringed = stringed[:-1]
        return answer

    def _decrypt(self, encrypted):
        answer = ""
        stringed = str(encrypted)
        while len(stringed) > 0:
            for pos in range(len(self._TABLE)):
                if self._TABLE[pos] == stringed[-1]:
                    equiv = str(self._TABLE[pos-2])
            answer = answer + equiv
            stringed = stringed[:-1]
        return answer

if __name__ == '__main__':
    m = Model()
    print(m._encrypt("1234"))
    print(m._decrypt("5248"))