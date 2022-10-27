# Introducing Narcotics Tracker v0.2.5.

| Version | Release Date | Audience   |
| :------ | :----------- | :--------- |
| 0.2.5   | ??/??/2022   | Developers |

**Message from ScottSucksAtProgramming:**

> Welcome to the Newly Refactored version of the Narcotics Tracker. After
> version 0.2.0 the code was quite a bit of a mess. I focused on restructuring
> the code and reducing coupling. The ultimate effect is code which is much
> more pleasant to work with and easier to understand. Read on to see the
> larger changes.

## Structural Changes

### Interfaces

### Builders Package

This package contains modules which can be used to build all of the DataItems
which are stored within the SQLite3 database. Full documentation is available
within that package and its modules. The previous templates were removed and
replaced with a single BuilderInterface class and modules for each of the six
DataItems.

The number of tests for this package has been greatly reduced due to the change
in responsibility of the DataItems class. Many tests for those behaviors have
been moved to the other parts of the test suite.

### Items Package

This package contain the modules for all items which are stored within the
database. The DataItem class defines an interface for all Data Items.

The number of tests for this package has been reduced and are available within
the Items sub-package within the Unit Tests package.

### Services Package

The services package was created to contain all the services and utilities
which are used to run the Narcotics Tracker. As of this release are three
service providers in this package: The Conversion Manager, Datetime Manager,
and SQLiteManager. Additionally the ServiceProvider class offers an object
which instantiates these services in a single command.

#### Intended Use

## Command Pattern

The **Command Design Pattern** was implemented to interact with the SQLite3
database.

### Receivers

All modules related to communications with SQLite3 have been moved into the
**Persistence Package**. The Database module contains the **SQLiteManager**
which sends and receives information from the database. It's designed to be
used as a context manager, and handles closing of the database connection
automatically. The Date Manager module contains the **DateTimeFormatter** which
returns the current datetime from the database and converts between a unix
timestamp and a human-readable date formatted as (MM-DD-YYYY HH:MM:SS).

## Invokers

Not yet implemented.

## Interface

The interface for SQLite3 Commands is located in the
`sqlite_command_interface.py` module.

## Commands

Commands are located within the `commands.py` module.
