import csv

def get_data(file_name):
    """ Load the data into a list

    Args:
        file_name    The name of the file containing the data (the ranked list)

    Returns:
        data         A list of items in ranked order
    """

    # Do something
    return []

def save_data(data, type, file_name):
    """ Save the data into a csv file

    Args:
        data         A list containing the items to save
        file_name    The name of the file to contain the data
    Returns:
        Nothing
    """

    fields = [type.replace(" ", "_")]

    with open("data/" + file_name, "w") as file:
        write = csv.writer(file)
        write.writerow(fields)
        for item in data:
            write.writerow([item])
