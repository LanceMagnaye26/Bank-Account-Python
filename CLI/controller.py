from view import View
from model import Model
import sys


class Controller():
    def __init__(self):
        self.view = View()
        self.model = Model()

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


    def run(self):
        teller_cred = self.view.get_teller_cred_msg().title()
        while teller_cred != 'q' or teller_cred != 'quit':
            while self.model.no_teller_check(teller_cred) != True:
                self.view.wrong_username_msg()
                teller_cred = self.view.get_teller_cred_msg().title()
            teller_pass = self.view.get_teller_pass_msg()
            while self.model.teller_password_check(teller_cred, teller_pass) != True:
                self.view.wrong_pass_msg()
                teller_pass = self.view.get_teller_pass_msg()
            self.view.main_menu()
            inp = self.view.choice_msg()
            while inp != '-q':
                if inp == '-c':
                    fname = self.view.get_fname_msg()
                    lname = self.view.get_lname_msg()
                    pin = self.view.get_pin_msg()
                    while self.model.pin_value_check(pin) == False:
                        self.view.value_error_msg()
                        pin = self.view.get_pin_msg()
                        while self.model.check_length(pin) != True:
                            self.view.pin_length_check_msg()
                            pin = self.view.get_pin_msg()
                    self.model.add_account(fname, lname, pin)
                    self.view.add_success_msg()
                self.view.main_menu()
                inp = self.view.choice_msg()



if __name__ == '__main__':
    controller = Controller()
    controller.run()
