"""Integration tests for handling Events in the SQlite3 database.

Classes:
    Test_EventStorage: Tests Event Storage in the SQLite3 database.

Functions:
    return_ids: Returns id numbers of DataItems obtained from the database.

"""

import sqlite3

from narcotics_tracker import commands
from narcotics_tracker.services.sqlite_manager import SQLiteManager


def return_ids(cursor: sqlite3.Cursor) -> list[int]:
    """Returns id numbers of DataItems obtained from the database.

    Args:
        cursor (sqlite3.Cursor): A cursor containing results of a select query.

    Returns:
        ids (list[int]): A list of DataItem id numbers.
    """
    ids = []

    raw_data = cursor.fetchall()
    for item in raw_data:
        ids.append(item[0])

    return ids


def return_ids(cursor: sqlite3.Cursor) -> list[int]:
    """Returns id numbers of DataItems obtained from the database.

    Args:
        cursor (sqlite3.Cursor): A cursor containing results of a select query.

    Returns:
        ids (list[int]): A list of DataItem id numbers.
    """
    ids = []

    raw_data = cursor.fetchall()
    for item in raw_data:
        ids.append(item[0])

    return ids


class Test_EventStorage:
    """Tests Event Storage in the SQLite3 database.

    Behaviors Tested:
        - Events can be added to the events table.
        - Events can be removed from the inventory table.
        - Events can be read from the inventory table.
        - Events can be updated.
        - Event's Modifier can be returned.
    """

    def test_events_can_be_added_to_db(self, reset_database, test_event) -> None:
        test_event = test_event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()

        commands.AddEvent(sq_man).set_event(test_event).execute()

        cursor = sq_man.read(table_name="events")
        event_ids = return_ids(cursor)
        assert -77 in event_ids

    def test_events_can_be_removed_from_db_using_ID(self, reset_database, test_event):
        test_event = test_event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.AddEvent(sq_man).set_event(test_event).execute()

        commands.DeleteEvent(sq_man).set_id(-1).execute()

        cursor = sq_man.read(table_name="events")
        event_id = return_ids(cursor)
        assert -1 not in event_id

    def test_events_can_be_removed_from_db_using_code(self, reset_database, test_event):
        test_event = test_event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.AddEvent(sq_man).set_event(test_event).execute()

        commands.DeleteEvent(sq_man).set_id("TEST").execute()

        cursor = sq_man.read(table_name="events")
        event_id = return_ids(cursor)
        assert -1 not in event_id

    def test_events_can_be_read_from_db(self, reset_database, test_event):
        test_event = test_event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.AddEvent(sq_man).set_event(test_event).execute()

        data = commands.ListEvents(sq_man).execute()

        assert data != None

    def test_events_can_be_updated_in_db(self, reset_database, test_event) -> None:
        test_event = test_event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.AddEvent(sq_man).set_event(test_event).execute()

        commands.UpdateEvent(sq_man).set_data(
            data={"event_code": "NEW CODE"}, criteria={"event_code": "TEST"}
        ).execute()

        returned_event = (
            commands.ListEvents(sq_man).set_parameters({"id": -77}).execute()[0]
        )

        assert "NEW CODE" in returned_event

    def test_event_modifier_can_be_returned(self, reset_database, test_event) -> None:
        test_event = test_event
        sq_man = SQLiteManager("data_item_storage_tests.db")
        commands.CreateEventsTable(sq_man).execute()
        commands.AddEvent(sq_man).set_event(test_event).execute()

        results = commands.event_commands.ReturnEventModifier(sq_man).execute("TEST")
        assert results == 999

    def test_event_modifier_can_be_returned(self, reset_database, test_event) -> None:
        # test_event = test_event
        # sq_man = SQLiteManager("data_item_storage_tests.db")
        # commands.CreateEventsTable(sq_man).execute()
        # commands.AddEvent(sq_man).set_event(test_event).execute()

        results = commands.event_commands.ReturnEventModifier().set_id("USE").execute()
        assert results == -1
