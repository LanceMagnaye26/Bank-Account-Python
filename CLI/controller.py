from view import View
from model import Users
from model2 import Managers
import sys


class Controller():
    def __init__(self):
        self.view = View()
        self.model = Users()
        self.managers = Managers()
        self.Users = Users()

    def pin_value_error_check(self):
        check = False
        while check != True:
            pin = self.view.get_pin_msg()
            if pin == 'cancel':
                sys.exit(0)
            try:
                pin = int(pin)
                if self.check_length(4, len(str(pin))) != False:
                    check = True
                    return pin
                else:
                    self.view.pin_length_check_msg()
            except ValueError:
                self.view.value_error_msg()

    def check_length(self, expected_length, actual_length):
        if actual_length != expected_length:
            return False

    def run(self):
        #get manager id and password
        inp = self.view.get_manager_id()
        if inp in self.managers.managers:
            passinp = self.view.get_manager_password()
            if passinp == self.managers.managers[inp]['Password']:
                # loop
                option = ''
                while option != 'quit' and option != 'q':
                    # show options
                    option = self.view.main_menu()
                    # user choses an option and it gets exicuted
                    if option == '-n' or option == '1':
                        self.view.creating_account_msg()
                        fname = self.view.get_user_fname()
                        lname = self.view.get_user_lname()
                        pin = self.pin_value_error_check()
                        self.model.add_account(fname, lname, pin)
                    elif option == '-d' or option == '2':
                        print(self.Users.accounts)
                        # inp =
                        self.view.deleting_account_msg()
                        acc_num = str(self.view.get_acc_num())
                        pin = self.pin_value_error_check()
                        if acc_num in self.Users.accounts:
                            if pin == self.Users.accounts[acc_num]['PIN']:
                                self.model.del_account(acc_num)
                            else:
                                self.view.inc_pin_msg()
                        else:
                            self.view.no_user_msg()
                    elif option == '-m' or option == '3':
                        print('not implimented yet')
            else:
                self.view.inc_pin_msg()
        else:
            self.view.no_user_msg()



if __name__ == '__main__':
    controller = Controller()
    controller.run()
