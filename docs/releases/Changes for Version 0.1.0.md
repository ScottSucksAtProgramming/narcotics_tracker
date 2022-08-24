# Sayonara, Narcotics Tracker v0.0.0. Long live version 0.1.0!!

| Version | Release Date |  Audience  |
| :------ | :----------- |:-----------|
| 0.1.0   |  08/01/2022  | Developers |

{{TOC}}

**Message from ScottSucksAtProgramming:**

> Hey! Thanks for checking out the changes coming to the Narcotics Tracker! This project is aimed at simplifying the tracking of controlled substance inventories for EMS agencies in New York State. This project is in still its infancy but I am proud to release the first major update having to do with Medications!

## Create your agency’s medications.
To keep track of the controlled substance inventory the **Narcotics Tracker** needs to know which medications are used at your EMS agency. 

The Medication and Builder Module makes creating and saving medications easy by using a stepwise approach to assign medication attributes. 

Medications that have been saved can be loaded from their data and updated as necessary to keep them up to date.

## Start building your agency’s database.

Your medications need to live somewhere. I built the database module to make connecting and interacting with the database a snap.

The Setup Script will create the table needed to store all data for the medications. If you want to manage tables yourself all the tools you need are contained within the database module.

## Containers, statuses, and units.

A set of options have been defined within the Enums package which can be used to set various attributes for your medications. 

Conversion between different dosage units is handled by the Unit Conversion module. You never have to worry about misplacing a decimal again.

## Develop additional features without fear using the test suite!

Each module has its own test suite containing almost 80 tests to ensure all parts of the code are working as intended. 

Running tests ensure that future updates to the project do not break any previous features and identify specific issues. Play and develop without fear.