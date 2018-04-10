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

    def del_account(self, acc_num):
        self.read_file()
        for user in range(len(self.accounts)):
            # print(self.accounts[user])
            if self.accounts[user]['Account Number'] == acc_num:
                self.accounts.pop(user)


if __name__ == '__main__':
    lance = Model()
    lance.add_account('New', 'User', 1234)
    # print(m.accounts)
    # print(m.accounts)