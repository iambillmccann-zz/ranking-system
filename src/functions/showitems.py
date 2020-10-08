from src.functions.mainmenu import clear_console

def print_header():
    """ Display a label on the console

    Args:
        None
    Returns:
        None
    """
    print('\n-----------------------------------------------------------------------')
    print('                          S H O W  I T E M S')
    print('-----------------------------------------------------------------------')

def print_items(data):
    """ Display the list

    Args:
        Data       The list of items to display
    Returns:
        None
    """
    rank = 0
    for item in data:
        rank += 1
        print("{rank}.  {item}".format(rank = rank, item = item))

def show_items(data):
    """ Display the ranked list

    Args:
        data   The list to display
    Returns:
        None
    """

    clear_console()
    print_header()
    print_items(data)

    input("\nPress the Enter key to continue ")