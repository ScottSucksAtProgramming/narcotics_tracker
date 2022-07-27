# Narcotics Tracker Design Document

## Summary

---

The Narcotics Tracker is a python project designed to assist controlled
substance agents for EMS organizations in New York State with controlled
substance inventory tracking, and reporting.

### Goal

To create an easy to use program which tracks an EMS agency's controlled
substance inventory, performs conversions between different units of weight
(i.e. mcg to mg), conversion between units of weight and units of volume
(mg/mcg to mL), track inventory totals throughout controlled substance
purchases, destruction via reverse distribution, medication waste, and
restocking of stock and sub-stocks. Reports can be generated as needed

## Motivation

---

I work as a controlled substance agent for a New York State Ambulance company.
While there have never been a concern of lost or diverted medications at my
agency the reporting, and license renewals which needs to be performed
periodically are always a source of stress. Documentation issues, incorrectly
stored paperwork, unit conversions and simple math mistakes are the most common
causes of reporting discrepancies. A simple software solution which can handle
those problems without human error will be personally useful.

I am also a self-taught programmer looking to increase my knowledge by building
out projects which are practical and can make my life easier. My personal
learning goals for this project are to increased my knowledge and experience
with Python; Learn about Object Oriented Programming; Practice and gain
experience with Test Driven Development; Gain knowledge on the storage, and
manipulation, of data. Opportunities to learn front-end development may arise
going forward as well.

## Screenshots

---

## Design Discussion and Alternatives

---

### Design Questions and Problems

#### Development Roadmap / Progress

I'm not entirely sure where the best place to begin is. I do not have a enough
experience to know how to design this kind of software. I'll be using a lot of
trial and error. Here is my imagined development Path.

-   [ ] Store and return medication related information.

#### Medication Class

I will need a class to handle medication objects which stores the various
properties related to each medication.

-   Properties

    -   Name
    -   Manufacturer
    -   NDC Number
    -   Container Type
    -   Box Quantity
    -   Fill Amount
    -   Dosage
    -   Concentration
    -   Unit

-   Methods

    -   I'm not sure what methods should go here.
