
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

    def get_user_pass(self):
        return input('Enter password: ')

    def get_user_fname(self):
        return input('Enter your first name: ')

    def get_user_lname(self):
        return input('Enter your last name: ')

    def get_manager_id(self):
        return input('Enter your ID: ')

    def get_manager_password(self):
        return int(input('Enter your password: '))

    def get_acc_num(self):
        return int(input('Enter an Account number: '))

    def main_menu(self):
        print('Choose what you would like to do:\n'
              '\t1. -c Create an account\n'
              '\t2. -d Delete an account\n'
              '\t3. -m Manage an account')
        return input()


if __name__ == "__main__":
    pornhub = View()

