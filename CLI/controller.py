from CLI.view import View
from CLI.model import Model
import sys


class Controller():
    def __init__(self):
        self.view = View()
        self.model = Model()

    def value_error_check(self, user_inp):
        check = False
        while check != True:
            try:
                inp = int(user_inp)
                check = True
            except ValueError:
                self.view.value_error()
                break
        print(check)
        return inp

    def run(self):
        if sys.argv[1] == '-c':
            if len(sys.argv) == 4:
                self.view.creating_account()
                pin = self.value_error_check(self.view.get_pin())
            else:
                self.view.parameter_error()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
