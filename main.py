# main.py
#
# This is a console application that sorts or ranks a list of things based on a subjective rating by the
# user.

from src.functions.configuration import get_configuration

if __name__ == "__main__":

    print("Hello World")
    print(get_configuration(file_name = "./test_bad_config.json"))
    