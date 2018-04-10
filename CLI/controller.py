from CLI.view import View
from CLI.model import Model
import sys


class Controller():
    def __init__(self):
        self.view = View()
        self.model = Model()

    def pin_value_error_check(self):
        check = False
        while check != True:
            try:
                pin = int(self.view.get_pin())
                if self.check_length(4, len(str(pin))) != False:
                    check = True
                    return pin
                else:
                    check = False
            except ValueError:
                self.view.value_error()

    def check_length(self, expected_length, actual_length):
        if actual_length != expected_length:
            self.view.pin_length_check()
            return False

    def run(self):
        if sys.argv[1] == '-c':
            if len(sys.argv) == 4:
                self.view.creating_account()
                pin = self.pin_value_error_check()
            else:
                self.view.parameter_error()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
