"""
This module is an ATM simulator.
It lets a user access his account with a password.
Then the user can see his balance, withdraw money and change its password.
"""

password = 4231
balance = 100


def authenticate_user():
    """
    Authenticates the user by taking password input.
    :return: True if user inputted correct password, False if not.
    """
    print("-" * 30)
    user_password = input("Please enter your password: ")
    if not user_password.isnumeric() or password != int(user_password):
        print("Wrong password")
        return False

    print("Login succeeded")
    return True


def take_menu_action_input(num_of_options):
    """
    Takes input from the user to determine his selection from menu options (every option has a number, starting at 0).
    The input is forced to be one of the options.
    :param num_of_options: The number of options in the menu.
    :return: The selected option.
    """
    user_selection = input("Enter the number of the desired action: ")
    while not user_selection.isnumeric() or not (num_of_options - 1 >= int(user_selection) >= 0):
        user_selection = input("You didn't enter a valid action number. Please enter again: ")

    return int(user_selection)


def handle_menu():
    """
    Handles the main atm menu.
    Displays the options, takes the users' input and calls the correct function.
    """
    menu_messages = ["Display balance", "Withdraw money", "Change password", "Exit program"]
    menu_functions = []

    print("-" * 30)
    for i, message in enumerate(menu_messages):
        print(f"{i} - {message}")

    user_selection = take_menu_action_input(len(menu_functions))


def main():
    """
    The main function of the module.
    Operates an infinite loop in which it authenticates the user and then creates the menu.
    """
    while True:
        if authenticate_user():
            handle_menu()


if __name__ == "__main__":
    main()
