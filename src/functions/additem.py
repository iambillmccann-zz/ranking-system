from src.functions.mainmenu import clear_console

def print_header():
    """ Display a label heading on the console

    There is no unittest coverage for this function

    Args:
        None

    Returns:
        None
    """
    print('\n-----------------------------------------------------------------------')
    print('                            A D D  I T E M')
    print('-----------------------------------------------------------------------')

def add_item(data, type):
    """ Add an item to the data in ranked order

    This function handles the process of adding an item to the list. It
    first requests the item from the console. Items are nothing more than a
    line of text typed in. Next, this kicks off a type of binary search to 
    find the proper location of the new item. Then it adds the item to 
    the data and lastly it prompts to add another.

    Args:
        data      The original list of items
        type      A label describing the type of items being ranked

    Returns
        A new list containing the new item
    """

    # prompt for item
    clear_console()
    print_header()
    prompt_message = "Add something new for {type} ==> ".format(type = type.lower())
    thing = input(prompt_message)

    # search for placement

    # add to list
    data.append(thing)

    # prompt for another

    return data