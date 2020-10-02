# main.py
#
# This is a console application that sorts or ranks a list of things based on a subjective rating by the
# user.

from src.functions.configuration import get_configuration
from src.functions import mainmenu

EXIT = "x"

# There is no unittest coverage for __main__

if __name__ == "__main__":

    mainmenu.clear_console()
    print('\n-----------------------------------------------------------------------')
    print('This is the Simple Ranking Program')
    print('Use this to rank items based on any subjective reason. The program works')
    print('by prompting for the item, and then asking to rate it against other items')
    print('in the list.')
    print('')
    print('copyright William McCann 2020')
    print('-----------------------------------------------------------------------')

    type, file = get_configuration()

    choice = mainmenu.get_user_input()
    while choice != EXIT:
        mainmenu.clear_console()
        choice = mainmenu.get_user_input()

    print('\n-----------------------------------------------------------------------')
    print('Goodbye.')
    print('-----------------------------------------------------------------------')
    