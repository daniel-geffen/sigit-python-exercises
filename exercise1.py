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


def main():
    """
    The main function of the module.
    Operates an infinite loop in which it authenticates the user and then creates the menu.
    """
    while True:
        if authenticate_user():
            pass


if __name__ == "__main__":
    main()
