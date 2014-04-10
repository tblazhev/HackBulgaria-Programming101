import sql_manager
from getpass import getpass


def help_main():
    print("Current valid commands:")
    print("login - for logging in!")
    print("register - for creating new account!")
    print("exit - for closing program!")


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = getpass("Enter your password: ")
            while sql_manager.check_for_strong_password(password) is False:
                print("Password is too weak. Use at least 9 characters, uppercase, lowercase, numeric and special characters.")
                password = input("Enter your password: ")

            sql_manager.register(username, email, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            help_main()

        elif command == 'exit':
            break
        else:
            print("Not a valid command")
            help_main()


def help_logged():
    print("Current valid commands:")
    print("info - for showing account info")
    print("change-password - change your password")
    print("change-message - for changing users message")
    print("show-message - for showing users message")
    print("exit - for closing program!")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        # elif command == 'changepass':
        #     new_pass = getpass("Enter your new password: ")
        #     while sql_manager.check_for_strong_password(new_pass) is False:
        #         print("Password is too weak. Use at least 9 characters, uppercase, lowercase, numeric and special characters.")
        #         new_pass = getpass("Enter your password: ")

        #     sql_manager.change_pass(new_pass, logged_user)

        elif command == "change-password":
            sql_manager.send_change_password(logged_user)
            verification_code = input("Enter verification code:")
            if not sql_manager.is_valid_verification_code(logged_user, verification_code):
                print("Invalid/Expired verification code.")
                continue

            new_password = getpass("Enter your new password: ")
            while sql_manager.check_for_strong_password(new_password) is False:
                print("Password is too weak. Use at least 9 characters, uppercase, lowercase, numeric and special characters.")
                new_password = getpass("Enter your new password: ")
            sql_manager.change_pass(logged_user, new_password)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            help_logged()

        elif command == 'exit':
            break

        else:
            print("Not a valid command")
            help_logged()


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
