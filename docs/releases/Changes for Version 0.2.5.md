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

### Items Package

This package contain the modules for all items which are stored within the
database. The DataItem class defines an interface for all Data Items.

## Command Pattern

After learning about the **Command Design Pattern** it felt like a great way to
structure storing and retrieving data from the SQLite3 Database. It should
allow flexibility to create and extend the reporting module when that is
implemented.

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

Not yet implemented.

## Commands

Not yet implemented.
