import sql_manager
import getpass
# import re
import hashlib


class Start:

    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")

        while True:
            command = input("$$$>")

            if command == 'register':
                username = input("Enter your username: ")
                password = getpass.getpass(prompt='Password: ')
                if len((password)) < 8:
                    print('Password must be at least 8 symbols')
                elif len(password) >= 8:
                    upper = 0
                    numbers = 0
                    special = 0
                    for letter in str(password):
                        if letter.isupper():
                            upper += 1
                        elif letter.isdigit():
                            numbers += 1
                        elif letter in "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]":
                            special += 1
                    if upper == 0 or numbers == 0 or special == 0:
                        print("Password MUST have capital letters, and numbers and a special symbol")
                    elif username in password:
                        print("Username can't be a substring of password")
                    else:
                        # problem s tova, che obekt Start nqma atribut sha1
                        sql_manager.register(username, password=self.sha1.hexdigest())
                        print("Registration Successfull")

            elif command == 'login':
                username = input("Enter your username: ")
                # password = input("Enter your password: ")
                password = getpass.getpass(prompt='Password: ')

                logged_user = sql_manager.login(username, password)

                if logged_user:
                    self.logged_menu(logged_user)
                else:
                    print("Login failed")

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
            else:
                print("Not a valid command")


    def logged_menu(logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                sql_manager.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")

    def hash_password(self):
        salt = "jhsdf"
        self.sha1 = hashlib.sha1()
        self.message = self.password
        self.sha1.update(bytearray(self.password + salt, "utf-8"))
        # sha1.update(password.encode("utf-8")
        self.sha1.hexdigest()

sql_manager.create_clients_table()
h = Start()
h.main_menu()
