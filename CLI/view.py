
class View():
    def value_error_msg(self):
        print('Please enter a number for your choice')
        return

    def creating_account_msg(self):
        print('Welcome to account creation')

    def deleting_account_msg(self):
        print('Welcome to account deletion')

    def parameter_error_msg(self):
        print('Missing parameter')

    def get_pin_msg(self):
        return input('Please enter a PIN: ')

    def pin_length_check_msg(self):
        print('Pin has to have length of 4')

    def inc_pin_msg(self):
        print('Incorrect pin. Please run again!')

    def no_user_msg(self):
        print('User does not exist')

    def get_user_cred_msg(self):
        return input('Enter user credentials: ')

    def get_user_pass_msg(self):
        return input('Enter password: ')

    def main_menu(self):
        print('Choose what you would like to do:\n'
              '1. -c Create an account\n'
              '2. -d Delete an account\n'
              '3. -m Manage an account')



if __name__ == "__main__":
    pornhub = View()

