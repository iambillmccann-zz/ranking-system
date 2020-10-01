import json

CONFIG_FILE_NAME = "./configuration.json"

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
    except:
        print("The application could not read the configuration file.")
        raise IOError("The application could not read the configuration file.")
    else:
        print("All good")