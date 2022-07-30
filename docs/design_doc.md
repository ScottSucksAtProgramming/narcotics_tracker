# Narcotics Tracker Design Document

# Table of Contents

1. [Summary](#summary)
2. [Goal](#goal)
3. [Motivation](#motivation)
4. [Screen Shots](#screenshots)

<a name="summary"></a>

## Summary

The Narcotics Tracker is a python project designed to assist controlled
substance agents for EMS organizations in New York State with controlled
substance inventory tracking, and reporting.

<a name="goal"></a>

## Goal

To create an easy to use program which tracks an EMS agency's controlled
substance inventory, performs conversions between different units of weight
(i.e. mcg to mg), conversion between units of weight and units of volume
(mg/mcg to mL), track inventory totals throughout controlled substance
purchases, destruction via reverse distribution, medication waste, and
restocking of stock and sub-stocks. Reports can be generated as needed

<a name="motivation"></a>

## Motivation

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
going forward as well. <a name="screenshots"></a>

## Screenshots

<a name="discussion"></a>

# Design Discussion and Alternatives

---

<a name="problems"></a>

## Design Questions and Problems

#### Development Roadmap / Progress

I'm not entirely sure where the best place to begin is. I do not have a enough
experience to know how to design this kind of software. I'll be using a lot of
trial and error. Here is my imagined development Path.

-   [ ] Store and return medication related information.

# Medication Class

I will need a class to handle medication objects which stores the various
properties related to each medication.

### Properties

    -   Name
    -   Manufacturer
    -   Box Quantity
    -   Container Type
    -   Fill Amount (in ml)
    -   Strength (in mg)
    -   Concentration
    -   Dose Unit

### Behaviors

    -   Create new Medications
    -   Delete Medications
    -   Updated Medications
    -   Store Medications
    -   Return Medication Properties

## Medication Class Discussion

**NDC Number**

This was removed. It fits better in an inventory or Medication Lot class which
will be used to track physical medications, as opposed to just medication
properties which are handled in this class.

---

**Box Quantity**

I'm unsure if this needs to stay here. I'm going to leave it for now, but it's
more related to inventory tracking than just the medication. Right now this
class has a lot of arguments and I don't know if I want there to be so many.

---

**Container Type** Considering also moving this to another class. Maybe an
'Order' class or 'Lot' class which would be a building block for the inventory.

## Container Enum

The Container class specifies the acceptable types of containers which
medication can come in.

```python
Container.VIAL = "Vial"
Container.AMPULE = "Ampule"
Container.PRE_FILLED_SYRINGE = "Pre-filled Syringe"
Container.PRE_MIXED_BAG = "Pre-mixed Bag"
```

Other container types exist, but are unlikely to be used in EMS agencies.

## DoseUnit Enum

The DoseUnit class specifies the acceptable types of units for the medications.

```python
Container.MG = "mg"
Container.MCG = "mcg"
Container.G = "G"
```

# Database

I'm going to use SQLite3 for this project. It's built into Python, it is simple
enough to get started, it seems to be able to handle everything I'll need, and
I already watched a FreeCodeCamp course about SQLite3 on my drive home from
work tonight.

**Medication Library** Medications are going to need a place to live and be
stored.

**Inventory** The whole point is

## Database Design

Started sketching out the database design which helped clear up some of my
questions. Version one of the design located in the docs folder. Instead of
designing from the top down, I'm going to start designing from the user
interface up which I think will clear up the tasks and processes and inform the
database design.

[Database Design v1](https://github.com/ScottSucksAtProgramming/narcotics_tracker/blob/master/docs/database_design_v1.pdf)
