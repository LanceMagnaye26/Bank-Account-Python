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

    def check_length(self, expected_length, actual_length):
        if actual_length != expected_length:
            return False

    def run(self):
        inp = self.view.get_user_cred_msg()
        while inp != 'quit' and 'q':
            if sys.argv[1] == '-n':
                self.view.creating_account_msg()
                pin = self.pin_value_error_check()
                self.model.add_account(sys.argv[2], sys.argv[3], pin)
            elif inp == '-d':
                if self.model.no_user_check(sys.argv[2]) == False:
                    self.view.deleting_account_msg()
                    pin = self.pin_value_error_check()
                    if self.model.del_account(sys.argv[2], pin) != True:
                         self.view.inc_pin_msg()
                else:
                    self.view.no_user_msg()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
