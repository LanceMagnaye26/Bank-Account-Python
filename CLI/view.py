
class View():
    def value_error_msg(self):
        print('Please enter a number for your choice')
        return

    def get_pin_msg(self):
        return input('Please enter a PIN: ')

    def pin_confirm_msg(self):
        return input('Please confirm your PIN: ')

    def pin_length_check_msg(self):
        print('Pin has to have length of 4')

    def inc_pin_msg(self):
        print('Incorrect pin. Please try again!')

    def get_teller_cred_msg(self):
        return input('Enter user credentials: ')

    def get_teller_pass_msg(self):
        return input('Enter password: ')

    def wrong_pass_msg(self):
        print('Wrong password! Please try again!')

    def wrong_username_msg(self):
        print('Wrong username! Please try again!')

    def main_menu(self):
        print('\nCommands:\n1. -c Create an account\n2. -d Delete an account\n3. -m Manage an account\n4. -q Quit\n5. -h Help\n')

    def choice_msg(self):
        return input('Please choose what to do: ')

    def get_fname_msg(self):
        return input('Please enter your first name: ')

    def get_lname_msg(self):
        return input('Please enter your last name: ')

    def add_success_msg(self):
        print('Your account has been successfully created!')

    def welcome_create_acc_msg(self):
        print('\nWelcome to account creation!')



if __name__ == "__main__":
    pornhub = View()

