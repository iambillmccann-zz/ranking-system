
from os import system, name 

def clear_console():
    """ clear the screen

    This function clears the terminal screen.

    There is no unittest coverage for this funciton.

    Args:
        None

    Returns:
        None
    """ 

	# for windows 
    if name == 'nt': 
        _ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def show_menu():
    """ Display the menu choices on the screen

    This function simply displays the menu text on the screen. It does not
    accept input, clear the screen, or anything else.

    There is no unittest coverage for this function.

    Args:
        None

    Returns:
        None
    """
    print('\n-----------------------------------------------------------------------')
    print('                           M A I N  M E N U')
    print('-----------------------------------------------------------------------')
    print(' Choose one of the following:')
    print('')
    print(' 1. Add a new item to the list')
    print(' 2. Show the list')
    print('')
    print(' X. Exit')
    print('')
    print(' Type a 1, 2 or X and then press Enter')
    print('-----------------------------------------------------------------------')

def get_user_input():
    """ Get input from the user

    This function uses the console to get user input for the main menu.

    There is no unittest coverage for this function.

    Args:
        None

    Returns:
        None
    """

    show_menu()
    return input('Type your selection here ==> ').lower()