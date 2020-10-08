from src.functions.mainmenu import clear_console, print_header
from src.functions.showitems import print_items

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
    print("Hello World")
    input("\nPress the Enter key to continue ")