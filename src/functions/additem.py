import math
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

def is_greater(thing, item):
    """ Pick which item is higher ranking

    Prompt the user to choose which thing is better, or ranked higher

    Args:
        thing     The item being added to the list
        item      The item in the list being compared
    Returns:
        True if the thing is ranked higher, otherwise False
    """

    print("\nWhich item should be ranked higher (better)?")
    print("\n1. {thing}".format(thing = thing))
    print("2. {item}".format(item = item))
    choice = input("\nChoose 1 or 2 ==> ")
    while choice not in ['1', '2']:
        choice = input("Don't over think this, just type 1 or 2 and press Enter ==> ")
    return True if choice == '1' else False

def search_for_spot(thing, data, top, bottom):
    """ Find the placement for the next item

    Use a binary search technique to determine where the next item shall be inserted
    into the list.

    selected formula explained

        "top +"                    indexing is based from top
        "math.ceil"                after dividing by two, round up
        "(bottom - top + 1) / 2"   find the mid point
        "- 1"                      account for zero based indexing

    Args:
        thing      The item being added to the list
        data       The list the item is added to
        top        The highest point in the list where the thing may be inserted
        bottom     the lowest place in the list where the thing may be inserted
    Returns:
        Insertion point
    """

    if len(data) == 0: 
        return top
    elif top > bottom: 
        return top
    else:
        selected = top + math.ceil( (bottom - top + 1) / 2 ) - 1
        if is_greater(thing, data[selected]):
            return search_for_spot(thing, data, top, selected - 1)
        else:
            return search_for_spot(thing, data, selected + 1, bottom)

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
    prompt_message = "\nAdd something new for {type}, leave blank to quit ==> ".format(type = type.lower())
    thing = input(prompt_message)

    while thing != "":

        # search for placement
        place_at = search_for_spot(thing, data, 0, len(data) - 1)

        # add to list
        data.insert(place_at, thing)

        # prompt for another
        thing = input(prompt_message)

    return data