## Ranking System
This document describes a very simple system for ranking items in a list based on subjective criteria. As an example, a person might want to rank their favorite foods. The system will prompt for an item, food in this example, and will add it to a list in sorting on the fly.

### Configuration File
The program is driven by a configuration file that is managed manually outside the program. The configuration file is formatted as JSON and contains two properties. These are:
- **type**  The type of thing being ranked. In the example above, the type would by "Food".
- **file**  The name of the file where the final list is stored.

The configuration file is always named `configuration.json` and resides in the root directory.
