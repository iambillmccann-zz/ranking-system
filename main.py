# main.py
#
# This is a console application that sorts or ranks a list of things based on a subjective rating by the
# user.

import argparse
import os

from src.functions.additem import add_item
from src.functions.showitems import show_items
from src.functions.configuration import CONFIG_NAME, get_configuration
from src.functions.mainmenu import get_user_input, clear_console
from src.functions.datafile import get_data, save_data

EXIT = "x"
PROMPT = "Type your selection here ==> "
CONFIG_FILE_NAME = "configuration.json"
CONFIG_NAME = "games"

# There is no unittest coverage for __main__

if __name__ == "__main__":

    clear_console()
    print('\n-----------------------------------------------------------------------')
    print('This is the Simple Ranking Program')
    print('Use this to rank items based on any subjective reason. The program works')
    print('by prompting for the item, and then asking to rate it against other items')
    print('in the list.')
    print('')
    print('copyright William McCann 2020')
    print('-----------------------------------------------------------------------')

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help = "Select a configuration.")
    parser.add_argument("-f", "--file", help = "Specify a config file.")
    args = parser.parse_args()

    configuration = args.config if args.config else CONFIG_NAME                     # use the default configuration is none is given
    config_file = args.file if args.file else CONFIG_FILE_NAME                      # use the default configuration file if none is given
    config_file = config_file if os.path.isfile(config_file) else CONFIG_FILE_NAME  # use the default configuration file if other is not found

    type, file = get_configuration(configuration, config_file)
    data = get_data(file)

    choice = get_user_input(PROMPT)
    while choice != EXIT:
        if choice == "1": 
            data = add_item(data, type)
            save_data(data, type, file)
        if choice == "2": show_items(data)

        clear_console()
        choice = get_user_input(PROMPT)

    print('\n-----------------------------------------------------------------------')
    print('Goodbye.')
    print('-----------------------------------------------------------------------')
    