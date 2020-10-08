from src.functions.mainmenu import clear_console, print_header
from src.functions.showitems import print_items
from src.functions.additem import search_for_spot

DEFAULT_MESSAGE = "\nType the number of the item to re-rank, leave blank to quit ==> "

def rerank_this(item, data):
    """ Re-rank the item in the list data

    Args:
        item         The index to the item being re-ranked
        data         The list of items
    Returns
        The updated data
    """

    print("\nYou decided to re-rank number {rank}. {thing}.".format(rank = item + 1, thing = data[item]))
    confirm = input("Type 'Y' and press Enter if this is correct ==> ")

    if confirm.lower() in ['y', 'yes', 'yeah', 'ya', 'yep', 'yup']:
        thing = data.pop(item)
        place_at = search_for_spot(thing, data, 0, len(data) - 1)
        data.insert(place_at, thing)
    else:
        print("Oops. Sorry. Try that again.")
    return data

def rerank_items(data):
    """ Rerank an item

    This function sends an item through the ranking process a second time.

    Args:
        data      The list of items
    Returns:
        The updated list of items
    """

    clear_console()
    print_header('                        R E - R A N K  I T E M')
    print_items(data)

    valid_input = [str(index) for index in range(1, len(data) + 1)]
    prompt_message = DEFAULT_MESSAGE
    item = input(prompt_message)

    while item != "":

        if item in valid_input: data = rerank_this(int(item) - 1, data)   # Note, subtract 1 from item to make it zero based.
        print_items(data)
        prompt_message = DEFAULT_MESSAGE if item in valid_input else "\nLet's try this again, type the number of the item to re-rank, leave blank to quit ==> "
        item = input(prompt_message)