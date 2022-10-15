# Introducing Narcotics Tracker v0.2.5.

| Version | Release Date | Audience   |
| :------ | :----------- | :--------- |
| 0.2.5   | ??/??/2022   | Developers |

**Message from ScottSucksAtProgramming:**

> Hey! Thanks for looking at the release notes for version 0.2.0 of the

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
returns the current datetime from the database, convert a unixepoch datetime to
a readable string, and converts a readable string, formatted as MM-DD-YYYY
HH:MM:SS to a unixepoch integer.

## Invokers

Not yet implemented.

## Interface

Not yet implemented.

## Commands

Not yet implemented.
