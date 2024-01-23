# Introducing Narcotics Tracker v0.2.5.

| Version | Release Date | Audience   |
| :------ | :----------- | :--------- |
| 0.2.5   | 10/31/2022   | Developers |

**Message from ScottSucksAtProgramming:**

> Welcome to the Newly Refactored version of the Narcotics Tracker. After
> version 0.2.0 the code was quite a bit of a mess. I focused on restructuring
> the code and reducing coupling. The ultimate effect is code which is much
> more pleasant to work with and easier to understand. Read on to see the
> larger changes.

## Structural Improvements

### Interfaces

Most packages within the Narcotics Tracker now include an interface specifying
how new modules should be created. Interfaces are located in a separate
sub-package.

### Design Patterns

The Builder Pattern had already been implemented to make construction of
DataItems easier. With this update the Command Pattern was also implemented
allowing for the decoupling many modules. All commands share the same interface
allowing for easy creation of new commands. Look at the documentation in the
Commands Package for more information.

### Inheritance and DataClasses

The Items Package saw an overhaul in is structure. Each of the six DataItems
inherit from a DataItem superclass. DataItems are no longer responsible for
saving and loading themselves from the database, their only concern is to store
their data. Each DataItem is now written as a dataclass. These two change make
the code much simpler to read.

## New Functionality

### The Service Provider

The Utilities Package was removed and replaced with the services package. As of
this release three services are included in this package. The SQLiteManager
provides the persistence service which stores and retrieves information from
the SQLite3 database. To manage dates and times the DateTimeManager provides
the datetime service; This object is responsible for providing datetime
information and converting between human readable dates and unix timestamps.
The conversion service, provided by the ConversionManager, converts between
different units of mass and volume.

The Service Provider module instantiates each service as needed. It is a single
point of access for all current and future services. The Service Provider also
allows for each service manager to be replaced with new or different services
as needed.

## Next Up!

The next release will see the creation of the reporting functionality and a set
of general reports which are frequently used for narcotics management.
