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
        print("Type = {type} and file = {file}".format(type=data["type"], file=data["file"]))
    except IOError:
        print("The application could not read the file {file_name}.".format(file_name = file_name))
        raise
    except:
        print("Cannot process the file {file_name}.".format(file_name = file_name))
        raise
    else:
        print("All good")
        return data["type"]