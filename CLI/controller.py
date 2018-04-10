from CLI.view import View
from CLI.model import Model
import sys


class Controller():
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):
        if sys.argv[1] == '-c':
            if len(sys.argv) == 4:
                self.view.creating_account()
                try:
                    pin = int(input(self.view.get_pin()))

                except ValueError:
                    self.view.value_error()

            else:
                self.view.parameter_error()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
