
class View():
    def value_error(self):
        print('Please enter a number for your choice')
        return

    def creating_account(self):
        print('Welcome to Account Creation')

    def parameter_error(self):
        print('Missing parameter')

    def get_account(self):
        pass

    def get_pin(self):
        return input('Please enter a PIN: ')

    def get_fname(self):
        return input('Please enter a Name: ')

    def get_lname(self):
        return input('Please enter a Name: ')

    def get_choice(self):
        return input('Please enter a Option: ')

    def pin_length_check(self):
        print('Pin has to have length of 4')




if __name__ == "__main__":
    pornhub = View()

    pornhub.main_menu()