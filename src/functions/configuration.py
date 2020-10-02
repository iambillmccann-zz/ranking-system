import json

CONFIG_FILE_NAME = "configuration.json"

def get_configuration(file_name = CONFIG_FILE_NAME):
    """Get the app's configuration
    
    Retrieve the configuration variables from the configuration file.
    
    Args:
        file_name    The fully qualified name of the configuration file. The default
                     is configuration.json.

    Returns:
        A tuple containing the value for the type and the name of the data file.
    """
    
    try:

        file = open(file_name,) 
        data = json.load(file)
        file.close()

        # The following print statements will throw exceptions if the json if not formatted
        # correctly. The same affect can be achieved by assigning variables.
        print("\nThis program is setup to rank {type}".format(type = data["type"]))
        print("The results will be kept in the file named {file}".format(file = data["file"]))

    except IOError:
        print("The application could not read the file {file_name}.".format(file_name = file_name))
        raise
    except:
        print("Cannot process the file {file_name}.".format(file_name = file_name))
        raise
    else:
        return (data["type"], data["file"])
