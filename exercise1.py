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


def display_balance():
    """
    Displays the users' balance.
    """
    print(f"Your balance is ${balance}")


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


def take_integer_input(name):
    """
    Takes input from the user. Forces the input to be a positive integer.
    :param name: The name of the object input is taken for.
    :return: The positive integer from the user.
    """
    user_input = input(f"Enter {name} (must be a positive integer): ")
    while not user_input.isnumeric():
        user_input = input(f"You entered {name} that isn't a positive integer. Please try again: ")
    return int(user_input)


def withdraw_amount(amount):
    """
    Withdraws a certain amount from the users' account.
    If the user doesn't have enough money it lets him know.
    :param amount: The amount to withdraw.
    """
    global balance
    if balance >= amount:
        balance -= amount
    else:
        print("Sorry, you don't have enough money to withdraw this amount.")


def withdraw_money():
    """
    Displays a menu for users to withdraw money from their account.
    The user selects a set amount or writes a custom amount to withdraw.
    Then the amount is withdrawn from the account.
    """
    withdraw_options = [20, 50]
    for i, amount in enumerate(withdraw_options):
        print(f"{i} - Withdraw {amount}")
    print(f"{len(withdraw_options)} - Withdraw custom amount")

    user_selection = take_menu_action_input(len(withdraw_options) + 1)  # Including custom option.
    if user_selection == len(withdraw_options):
        amount = take_integer_input("an amount to withdraw")
    else:
        amount = withdraw_options[user_selection]

    withdraw_amount(amount)


def change_password():
    """
    Takes a new password from the user and updates it.
    """
    new_password = take_integer_input("a new password")

    global password
    password = int(new_password)
    print("Your password was successfully changed")


def handle_menu():
    """
    Handles the main atm menu.
    Displays the options, takes the users' input and calls the correct function.
    """
    menu_messages = ["Display balance", "Withdraw money", "Change password", "Exit program"]
    menu_functions = [display_balance, withdraw_money, change_password, exit]

    print("-" * 30)
    for i, message in enumerate(menu_messages):
        print(f"{i} - {message}")

    user_selection = take_menu_action_input(len(menu_functions))

    menu_functions[user_selection]()


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
