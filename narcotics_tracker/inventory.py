"""Defines the representation of the inventory table and inventory events.

This module handles the creation of the inventory table. The Events class 
defines the representation of the events or lines in the inventory which will 
adjust the actual inventory amounts. 

See the database module for information on interacting with the database.
Tests are located in the tests/unit/inventory_test.py file.

Classes:

    Events: Defines the events that adjust the inventory amounts.

Functions:

    return_table_creation_query: Returns query to create medication table.

    #! parse_medication_data: Returns medication data from database as dictionary.
"""
