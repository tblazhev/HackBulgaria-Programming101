import sql_manager
from getpass import getpass


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

        # elif command == 'changepass':
        #     new_pass = getpass("Enter your new password: ")
        #     while sql_manager.check_for_strong_password(new_pass) is False:
        #         print("Password is too weak. Use at least 9 characters, uppercase, lowercase, numeric and special characters.")
        #         new_pass = getpass("Enter your password: ")

        #     sql_manager.change_pass(new_pass, logged_user)

        elif command == "send-reset-password":
            sql_manager.send_reset_password(logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            #print("changepass - for changing passowrd")
            print("send-reset-password - send a random code for password reset")
            print("reset-password - insert a code for changing your password")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("exit - for closing program!")

        elif command == 'exit':
            break


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
