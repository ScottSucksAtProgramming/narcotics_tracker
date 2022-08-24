# 5 - Files and Directories

| File Version | Project Version | Created On | Modified On |
|:--|:--|:--|:--|
| 0.0.0 | 0.0.0 | 08/15/2022 | 08/15/2022

{{TOC}}

A well organized directory structure makes it easier to work with the code base. Here is the directory structure and important files used for the **Narcotics Tracker** project.


##  5.1 - Directory Structure

###### Directory Tree
```
.
├── assets
├── data
├── docs
│   ├── blog
│       └── published
│   ├── design
│   └── style_guide
│       └── checklists
├── narcotics_tracker
│   ├── builders
│   ├── enums
│   └── utils
├── scripts
├── tests
│   └── unit
└── venv
```
 
### 5.1.1 - `root/`
The root directory for the project.

###### Files
* `README.md` - The readme file for the project.
* `LICENSE.txt` - The license used for this project.
* `.gitignore` - List of files and folders which are not tracked by git source control.

### `narcotics_tracker/`
The `narcotics_tracker/` directory contains the python modules and packages for the **Narcotics Tracker**.

###### Packages
* `builders/` - Contains the modules which build objects.
* `enums/` - Contains the Enums used in the project.
* `utils/` - Contains utility functions which don’t fit elsewhere.

###### Modules
* `database.py` - Manages interactions with the SQLite3 database.
* `date.py` - Obtains and formats the dates needed for the database.
* `medication.py` - Handles medication objects within the project.

##### Modules vs. Packages

* Individual `.py` files are referred to as modules. They should be atomic and contain no more than one class. 
* Related modules should be combined into a package by grouping them within a subdirectory which includes a `__init__.py` file.
* Simplicity and ease of navigation is the guiding principle when creating packages.
* Use the naming structure defined in the [[naming]] portion of this style guide.

### 5.1.2 - `tests/`
The `tests/` directory contains all tests for the **Narcotics Tracker**. Tests are split into sub-directories related to their type. For organizational purposes it is recommended to put all tests related to a module or package into a single test module. A test module may contain multiple classes.

###### Packages
* `unit/` - Contains unit test modules.

###### Files
`conftest.py` - Configuration file for pytest.

### 5.1.3 - `scripts/`
The `scripts/` directory contains python modules which can be run on their own to excecute parts of the **Narcotics Tracker**.

###### Modules
* `create_medications.py` - Builds sample medications and writes them to the database.
* `setup.py` - Creates the tables used by the project in the database.

### 5.1.4 - `data/`
The `data/` directory contains the database files used for the project.

###### Database Files
* `inventory.db` - The main database file housing all tables and data for the **Narcotics Tracker**.
* `test_database.db` - The database files used to run the tests.

### 5.1.5 - `docs/`
The `docs/` directory contains all documentation and developer resources for the project.

###### Sub-directories
* `blog/` - Contains blog entries which narrate the development process for the **Narcotics Tracker**.
    * `published` - Contains finialized versions of the blog entries.
* `design` - Contains all documents related to the project’s design.
* `style_guide`  - Contains the style guide files for this project.
    * `checklists/` - Contains checklists which can be used to ensure the code fits the style guide.
###### Files
`design_doc.md` - The design doc and discussions for this project.
`requirements.txt` - The modules and packages required for the **Narcotics Tracker**.


### 5.1.6 - `assets/`
The `assests` directory contains images, videos and other media which are used as part of the project.

### 5.1.7 - `venv/`
The `venv/` directory contains the virtual environment used when buliding this project. For more information look at `docs/requirements.txt`.