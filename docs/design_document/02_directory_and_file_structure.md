# 0.2 - Directory and File Structure

| Section | Version | Created    | Updated    |
| :------ | :------ | :--------- | :--------- |
| 0.1     | 0.2.5   | 10/25/2022 | 10/25/2022 |

{{TOC}}



## Directory and File Structure
- `narcotics_tracker/` 
    - Project Repository Folder
    - `LICENSE.txt`
        - License Information
    - `README.md`
        - General Project Information
    - `assets/`
        - Media items used throughout project development.
    - `data/`
        - Project database directory.
    - `docs/`
        - `design_document/`
            - Markdown files outlining the design options and decisions made for the project.
        - `release_notes/`
            - Markdown files outlining the changes to the project throughout its development.
        - `style_guide/`
            - Markdown files outline the style guide for this project.
    - `narcotics_tracker/`
        - Project source code directories.
        - `database.py`
            - Handles communication directly with the SQLite3 Database.
        - `builders/`
            - Handles the construction of DataItems.
        - `commands/`
            - Handles higher-level program functions by using the Command design pattern.
        - `items/`
            - Defines the DataItems which enable inventory tracking.
        - `scripts/`
            - Miscellaneous scripts for setup and testing.
        - `setup/`
            - Contains setup and configuration files.
        - `utils/`
            - Miscellaneous helper and utility modules.
    - `tests/`
        - Testing Suite
        - `integration/`
            - Tests higher level features which require inter-related parts of the application.
        - `unit/`
            - Tests lower level features.
    - `venv/`
        - Project virtual environment files.

[Design Document Table of Contents](01_table_of_contents.md)