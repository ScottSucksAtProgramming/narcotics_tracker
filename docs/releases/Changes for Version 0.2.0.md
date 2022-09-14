# Introducing Narcotics Tracker v0.2.0. Now with 60% more tables!

| Version | Release Date | Audience   |
| :------ | :----------- | :--------- |
| 0.2.0   | 09/14/2022   | Developers |

**Message from ScottSucksAtProgramming:**

> Hey! Thanks for looking at the release notes for version 0.2.0 of the
> Narcotics Tracker. This release includes a lot of changes and added new
> functionality to track inventory changes of controlled substance medications.
> I have had the pleasure of learning a lot about Object Oriented Programming,
> software architecture and the
> [pleasure of writing documentation](https://giphy.com/gifs/bored-monsters-inc-RKS1pHGiUUZ2g)
>
> I've immensely enjoyed working on this project. The next update will focus on
> reorganizing the files and code to reduce coupling and better follow the
> Single Responsibility Principle. Following that a set of command line tools
> will be released for setting up the Narcotics Tracker on new systems and for
> interacting with the database.
>
> Any questions or comments are welcome please reach out to me via the Github
> Repository.

## New Database Objects added.

With version 0.2.0 you can now create multiple database objects needed for
controlled substance inventory management.

### Medications

Medications are the bread and butter of this project and are still created
using The Builder Pattern. They live in inside the medications table.

### Containers, Units and Statuses

Containers, Units and Statuses have been moved their own Vocabulary Control
Tables instead of Enums. This will allow for greater flexibility for users to
add and remove these items as necessary for their agencies.

### Events and Reporting Periods

Two brand new database objects were defined and created. Events describe the
type of event which caused a change in inventory such as patient
administration, waste, or ordering new medications.

Reporting Periods were created to help organize Adjustments into groups based
on when they need to be reported to the Department of Health and the Bureau of
Narcotics Enforcement.

### Adjustments

Adjustments were added as part of the Inventory Module. Events are the reason
that an inventory change occurred; Adjustments represent the actual changes.
Adjustments are logged into the inventory table of the database and either add
or remove an amount of a medication.

## Database Context Manager

The Database module and Database Class were updated to support their use as a
context manager.

Using the 'with' keyword will activate the context manager and ensure that the
connection to the database is closed regardless of any errors or failures
encountered. Please look at the documentation for these items for more
information on using then.

Example:

```python
with database.Database() as db:
    test_medication.save(db)
```

## Dates

The Date module was removed in favor of using the data functionality provided
by the SQLite3 package. Dates are now stored in the database as integers using
the unix epoch timestamp. This allows for dates to be compared against one
another and for Adjustments to be assigned the correct Reporting Period. It
also simplified the code.

Dates must be entered using the format 'YYYY-MM-DD HH:MM:SS' or 'YYY-MM-DD' and
are converted into unix epoch by the software.

## Test Suite

I have continued to use Test Driven Development and build out the test suite.
As of this release there are 260 unit tests available which run in less than
one second to ensure that all parts of the Narcotics Tracker are working as
expected.

## Next Release

The next release will focus on the building of command line tools which should
provide a 'Minimum Viable Product' and a restructure of the software design
focusing on the Single Responsibility Principle and greater use of Objects.
