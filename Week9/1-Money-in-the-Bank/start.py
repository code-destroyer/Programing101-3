import sql_manager
import getpass
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
                self.password = getpass.getpass(prompt='Password: ')
                self.email = input("Enter your email:")
                self.hash2_password = hashlib.sha1(self.password.encode('utf-8')).hexdigest()
                if len((self.password)) < 8:
                    print('self.password must be at least 8 symbols')
                elif len(self.password) >= 8:
                    upper = 0
                    numbers = 0
                    special = 0
                    for letter in str(self.password):
                        if letter.isupper():
                            upper += 1
                        elif letter.isdigit():
                            numbers += 1
                        elif letter in "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]":
                            special += 1
                    if upper == 0 or numbers == 0 or special == 0:
                        print("self.password MUST have capital letters, and numbers and a special symbol")
                    elif username in self.password:
                        print("Username can't be a substring of password")
                    else:
                        # problem s tova, che obekt Start nqma atribut sha1
                        logged_user = sql_manager.register(username, password=hash2_password)
                        print("Registration Successfull")

            elif command == 'login':
                self.username = input("Enter your username: ")
                # self.password = input("Enter your self.password: ")
                self.password = getpass.getpass(prompt='self.password: ')
                self.hash2_password = hashlib.sha1(self.password.encode('utf-8')).hexdigest()
                logged_user = sql_manager.login(self.username, self.hash2_password)

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


    def logged_menu(self, logged_user):
        logged_user = sql_manager.login(self.username, self.hash2_password)
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")
            user = logged_user.get_username()

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

            elif command == 'deposit':
                amount = input("Enter amount:")
                amount = float(amount)
                sql_manager.deposit(amount, user)

            elif command == 'withdraw':
                amount = input("Enter amount:")
                amount = float(amount)
                sql_manager.withdraw(amount, user)

            elif command == 'display':
                sql_manager.display(user)

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")
                print("deposit - deposit money in the bank account")
                print("withdraw - to withdraw money from the bank account")
                print("display - display balance of the bank account")

sql_manager.create_clients_table()
h = Start()
h.main_menu()
