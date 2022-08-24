"""This module will act as a setup script for the narcotics_tracker."""

from narcotics_tracker import medication


def create_medication_table(db_connection) -> None:
    """This function will create the medication table."""

    db_connection.create_table(medication.return_table_creation_query())


if __name__ == "__main__":
    create_medication_table()
