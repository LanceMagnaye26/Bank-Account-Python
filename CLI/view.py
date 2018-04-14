
class View:
    def value_error_msg(self):
        print('\nPlease enter a number for your choice')
        return

    def get_pin_msg(self):
        return input('\nPlease enter a PIN: ')

    def pin_confirm_msg(self):
        return input('\nPlease confirm your PIN: ')

    def pin_length_check_msg(self):
        print('\nPin has to have length of 4 or 6')

    def no_user_msg(self):
        print('\nUser does not exist')

    def inc_pin_msg(self):
        print('\nIncorrect pin. Please try again!')

    def pin_not_match(self):
        print('\nPins do not match. Please try again!')

    def get_teller_cred_msg(self):
        return input('\nEnter user credentials: ')

    def get_teller_pass_msg(self):
        return input('\nEnter password: ')

    def wrong_pass_msg(self):
        print('\nWrong password! Please try again!')

    def wrong_username_msg(self):
        print('\nWrong username! Please try again!')

    def main_menu(self):
        print('\nCommands:\n1. -c Create an account\n2. -d Delete an account\n3. -m Manage an account\n4. -q Quit\n5. -h Help')

    def manage_acc_menu(self):
        print('\nCommands:\n1. -d Deposit\n2. -w Withdraw\n3. -q Quit\n4. -h Help')

    def choice_msg(self):
        return input('\nPlease choose what to do: ')

    def invalid_choice_msg(self):
        print('\nInvalid option. Please choose option number 5 for help')

    def get_fname_msg(self):
        return input('\nPlease enter your first name: ')

    def get_lname_msg(self):
        return input('\nPlease enter your last name: ')

    def add_success_msg(self):
        print('\nYour account has been successfully created!')

    def del_success_msg(self):
        print('\nYour account has been successfully deleted')

    def welcome_create_acc_msg(self):
        print('\nWelcome to account creation!')

    def welcome_delete_acc_msg(self):
        print('\nWelcome to account deletion')

    def welcome_manage_acc_msg(self):
        print('\nWelcome to account management')

    def get_acc_num(self):
        return input('\nPlease enter an account number: ')

    def get_acc_mng(self):
        return input('\nPlease choose what to do with this account: ')

    def help_main_menu(self):
        print('\nPress -c to create a new account for a new user. The account will have both Chequing and Savings.'
              '\nPress -d to delete an existing account of a user in the database. This command will delete the whole account including Chequing and Savings.'
              '\nPress -m to manage an existing account of a user in the database.'
              '\nPress -q to quit the main menu and return to log in.'
              '\nPress -h for help and instructions.')

    def help_mng_acc_menu(self):
        print('\nPress -d to deposit money into this account.'
              '\nPress -w to withdraw money from this account. Overdraft up to $500 for Savings account type.'
              '\nPress -q to quit managing account section and return to main menu.'
              '\nPress -h for help and instructions.')