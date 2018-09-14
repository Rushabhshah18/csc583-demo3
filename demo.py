import sys

from manager.manager_user import UserManager


class Main(object):

    def _fetch_data(self):
        return raw_input()

    def _fetch_int(self):
        try:
            return int(raw_input())
        except ValueError:
            print("Please enter only numbers.")
            return self._fetch_int()

    def _print_menu(self):
        print("Please select your option")
        print("0.\tExit")
        print("1.\tCreate new user")
        print("2.\tFetch last user")
        print("3.\tFetch all users in database")

    def _fetch_moptions(self):
        menu = self._fetch_int()
        user_manager = UserManager()

        # Switch according to menu option
        if menu == 0:
            return False
        elif menu == 1:
            # Create new user selected
            print("Please input username(Remember it has to be unique)")
            usr = self._fetch_data()
            print("Please input password")
            pwd = self._fetch_data()
            user_manager.create_user(**{'usr': usr, 'pwd': pwd})
        elif menu == 2:
            # Fetch last user
            user = user_manager.fetch_last_user()
            if user:
                print("Username: " + user.username + "\t Password: " + user.password)
            else:
                print("No users in the database atm. Create one now from menu.")
        elif menu == 3:
            # Fetch all users
            users = user_manager.fetch_all_users()
            if users:
                for user in users:
                    print("Username: " + user.username + "\t Password: " + user.password)
            else:
                print("No users in the database atm. Create one now from menu.")
        else:
            print("Please select correct option. Try again")
            self._fetch_moptions()

        return True

    def __init__(self):
        print("###\nWelcome to CSC583 Demo 3\n###")
        while True:
            # Print menu and ask for action
            self._print_menu()
            if not self._fetch_moptions():
                break


if __name__ == '__main__':
    sys.exit(Main())
