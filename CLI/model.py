import csv
class Model():

    _NEXT_ACC_NUM = 1

    def __init__(self):
        self.filename = 'accounts.csv'
        self.accounts = []
        self.fieldnames = ['First Name', 'Last Name', 'Account Number', 'PIN', 'Balance']

    def write_file(self):
        with open(self.filename, 'w') as open_f:
            csv_writer = csv.DictWriter(open_f, fieldnames=self.fieldnames, delimiter=',')

            csv_writer.writeheader()

            for user in self.accounts:
                csv_writer.writerow(user)

    def read_file(self):
        try:
            with open(self.filename, 'r') as open_f:
                csv_reader = csv.DictReader(open_f)
                self.accounts = []
                for user in csv_reader:
                    self.accounts.append({'Account Number': user['Account Number'], 'First Name': user['First Name'], 'Last Name': user['Last Name'], 'PIN': user['PIN'], 'Balance': user['Balance']})
        except FileNotFoundError:
            self.write_file()


    def add_account(self, f_name, l_name, pin):
        self.read_file()
        if len(self.accounts) != 0:
            user_dict = {'Account Number': int(self.accounts[-1]['Account Number']) + 1, 'First Name': f_name, 'Last Name': l_name, 'PIN': pin, 'Balance':0}
        else:
            user_dict = {'Account Number': Model._NEXT_ACC_NUM, 'First Name': f_name, 'Last Name': l_name, 'PIN': pin, 'Balance':0}
        self.accounts.append(user_dict)
        self.write_file()
        # print(len(self.accounts))

    def del_account(self, acc_num, pin):
        self.read_file()
        check = False
        for user in self.accounts:
            if acc_num == user['Account Number']:
                if str(pin) == user['PIN']:
                    del self.accounts[self.accounts.index(user)]
                    check = True
        self.write_file()
        return check

    def no_user_check(self, acc_num):
        self.read_file()
        for user in self.accounts:
            if user['Account Number'] == str(acc_num):
                check = False
        return check

if __name__ == '__main__':
    m = Model()
    m.del_account(8, 1234)
    # print(m.accounts)
    # print(m.accounts)