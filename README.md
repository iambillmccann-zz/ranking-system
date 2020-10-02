## Ranking System
This document describes a very simple system for ranking items in a list based on subjective criteria. As an example, a person might want to rank their favorite foods. The system will prompt for an item, food in this example, and will add it to a list in sorting on the fly.

### Configuration File
The program is driven by a configuration file that is managed manually outside the program. The configuration file is formatted as JSON and contains two properties. These are:
- **type**  The type of thing being ranked. In the example above, the type would by "Food".
- **file**  The name of the file where the final list is stored.

The configuration file is always named `configuration.json` and resides in the root directory.

### Features
There are two functions in this system. These are:

- Add an item to the list
- Show the list

The application displays a simple console based menu where you choose the appropriate option. And actually there is a third option; quit.

The program displays a menu and the user enters an option, either 1, 2, or X. One is for adding itmes, two is for showing the list, and X exits the system.

### Unit Tests
This application is tested with Python's unittest framework. Test scripts are found in the `/tests` folders. I setup VSCode to find scripts suffixed with the word *test* so you  will find scripts with names like *setup_test.py*. The table below lists the unit test scripts:

| Source File      | Descriptions                                                 |
| ---------------- | ------------------------------------------------------------ |
| setup.py         | Simple string tests that verify the unittest framework has been properly setup. These tests do not affect the function of the ranking system. |
| configuration.py | This are test cases that verify the get_configuration() function works as designed. |

