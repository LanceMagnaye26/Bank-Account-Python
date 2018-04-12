import json

class Managers():

    _NEXT_ACC_NUM = 1000000

    def __init__(self):
        self.filename = 'managers.json'
        self.managers = {}
        self.read_file()

    def write_file(self):
        with open(self.filename, 'w') as open_f:
            json.dump(self.managers, open_f)

    def read_file(self):
        try:
            with open(self.filename, 'r') as open_f:
                self.managers = {}
                self.managers = json.load(open_f)
        except FileNotFoundError:
            self.write_file()


    def add_account(self, name, id, pin):
        self.read_file()
        self.managers[name] = {'UserID': id, 'Password': pin}
        self.write_file()

    def del_account(self, name):
        self.read_file()
        del self.managers[str(name)]
        self.write_file()