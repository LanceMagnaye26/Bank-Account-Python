
class View():
    def value_error_msg(self):
        print('Please enter a number for your choice')
        return

    def get_pin_msg(self):
        return input('Please enter a PIN: ')

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
        print('Choose what you would like to do:\n'
              '1. -c Create an account\n'
              '2. -d Delete an account\n'
              '3. -m Manage an account')



if __name__ == "__main__":
    pornhub = View()

