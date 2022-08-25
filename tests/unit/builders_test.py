"""Contains the Test_MedicationBuilder class used to test the module.

Classes: 

    Test_BuilderTemplates: Contains all unit tests for the template modules.

    Test_MedicationBuilder: Contains all unit tests for the module.

    Test_OrderBuilder: Contains all units tests for order_builder module.
"""
import pytest

from narcotics_tracker import medication
from narcotics_tracker import order
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import (
    medication_builder,
    medication_builder_template,
    order_builder,
    order_builder_template,
)


class Test_BuilderTemplates:
    """Contains all unit tests for the builder template modules.

    Behaviors Tested:
        - Can access medication_builder_template module.
        - Can access medication_builder Medication Class.
        - Can access order_builder_template module.
        - Can access order_builder_template Order Class.
    """

    def test_can_access_medication_builder_template_module(self) -> None:
        """Tests that the medication_builder_template module can be accessed.

        Asserts that medication_builder_template.__doc__ does not return 'None'.
        """
        assert medication_builder_template.__doc__ != None

    def test_can_access_medication_builder_Medication_class(self) -> None:
        """Tests that medication_builder_template.Medication can be accessed.

        Asserts that medication_builder_template..Medication.__doc__ does not
        return 'None'.
        """
        assert medication_builder_template.Medication.__doc__ != None

    def test_can_access_order_builder_template_module(self) -> None:
        """Tests that the order_builder_template module can be accessed.

        Asserts that order_builder_template.__doc__ does not return 'None'.
        """
        assert order_builder_template.__doc__ != None

    def test_can_access_order_builder_Order_class(self) -> None:
        """Tests that order_builder_template.Order can be accessed.

        Asserts that order_builder_template..Order.__doc__ does not
        return 'None'.
        """
        assert order_builder_template.Order.__doc__ != None


class Test_MedicationBuilder:
    """Contains all unit tests for the medication_builder module.

    Behaviors Tested:
        - Can access medication_builder module.
        - Can access MedicationBuilder class.
        - MedicationBuilder sets the medication id correctly.
        - MedicationBuilder sets the medication name correctly.
        - MedicationBuilder sets the medication code correctly.
        - MedicationBuilder sets the medication container correctly.
        - An exception is raised if the medication container is not valid.
        - MedicationBuilder sets the medication fill amount correctly.
        - MedicationBuilder sets the medication dose correctly.
        - MedicationBuilder sets the medication unit correctly.
        - An exception is raised if the medication unit is not valid.
        - MedicationBuilder sets the medication concentration correctly.
        - MedicationBuilder sets the medication status correctly.
        - An exception is raised if the medication status is not valid.
        - MedicationBuilder sets the medication created date correctly.
        - MedicationBuilder sets the medication modified date correctly.
        - MedicationBuilder sets the medication modified by correctly.
        - MedicationBuilder calculates the medication concentration correctly.
        - Created medication object has type medication.Medication.
    """

    def test_can_access_medication_builder_module(self) -> None:
        """Tests that the medication_builder module can be accessed.

        Asserts that medication_builder.__doc__ does not return 'None'.
        """
        assert medication_builder.__doc__ != None

    def test_can_access_MedicationBuilder_class(self) -> None:
        """Tests that MedicationBuilder can be accessed.

        Asserts that MedicationBuilder.__doc__ does not
        return 'None'.
        """
        assert medication_builder.MedicationBuilder.__doc__ != None

    def test_set_medication_id(self):
        """Tests that MedicationBuilder sets the medication id correctly.

        Asserts that the medication id returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 69420

        med_builder.set_medication_id(expected)

        assert med_builder.medication_id == expected

    def test_set_name(self):
        """Tests that the medication builder sets the name.

        Asserts the medication name returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "Aspirin"

        med_builder.set_name("Aspirin")

        assert med_builder.name == expected

    def test_set_code(self):
        """Tests that the medication builder sets the code.

        Asserts that the medication code returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "ASA"

        med_builder.set_code("ASA")

        assert med_builder.code == expected

    def test_set_container(self):
        """Tests that the medication builder sets the container type.

        Asserts that the medication container returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "Ampule"

        med_builder.set_container(containers.Container.AMPULE)
        assert med_builder.container_type.value == expected

    def test_set_container_raises_exception_if_invalid(self):
        """Tests that the medication builder raises an exception if invalid.

        Passes if an AttributeError exception is raised."""

        med_builder = medication_builder.MedicationBuilder()

        with pytest.raises(AttributeError):
            med_builder.set_container(containers.Container.INVALID)

    def test_set_fill_amount(self):
        """Tests that the medication builder sets the fill amount.

        Asserts that the medication fill amount returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 10_000

        med_builder.set_fill_amount(expected)

        assert med_builder.fill_amount == expected

    def test_set_dose(self):
        """Tests that the medication builder sets the dose and unit.

        Asserts that the medication dose returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 10_000

        med_builder.set_dose_and_unit(10, units.Unit.MG)

        assert med_builder.dose == expected

    def test_set_unit(self):
        """Tests that the medication builder sets the dose and unit.

        Asserts that the medication dose returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "mg"

        med_builder.set_dose_and_unit(10, units.Unit.MG)

        assert med_builder.unit.value == expected

    def test_set_unit_raises_exception_if_invalid(self):
        """Tests that the medication builder raises an exception if invalid.

        Passes if an AttributeError exception is raised.
        """
        med_builder = medication_builder.MedicationBuilder()

        with pytest.raises(AttributeError):
            med_builder.set_unit(units.Unit.INVALID)

    def test_set_concentration(self):
        """Tests that the medication builder sets the concentration.

        Asserts that the medication concentration returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 45

        med_builder.set_concentration(expected)

        assert med_builder.concentration == expected

    def test_set_status(self):
        """Tests that the medication builder sets the status.

        Asserts that the medication status returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()

        med_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)
        expected = "Active"

        assert med_builder.status.value == expected

    def test_set_status_raises_exception_if_invalid(self):
        """Tests that the medication builder raises an exception if invalid.

        Passes if an AttributeError exception is raised.
        """
        med_builder = medication_builder.MedicationBuilder()

        with pytest.raises(AttributeError):
            med_builder.set_status(medication_statuses.MedicationStatus.INVALID)

    def test_set_created_date(self):
        """Tests that the medication builder sets the created date.

        Asserts that the medication created date returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "01/01/2019"

        med_builder.set_created_date(expected)

        assert med_builder.created_date == expected

    def test_set_modified_date(self):
        """Tests that the medication builder sets the modified date.

        Asserts that the medication modified date returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "08/21/1986"

        med_builder.set_modified_date(expected)

        assert med_builder.modified_date == expected

    def test_set_modified_by(self):
        """Tests that the medication builder sets the modified by.

        Asserts that the medication modified by returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = "John Doe"

        med_builder.set_modified_by(expected)

        assert med_builder.modified_by == expected

    def test_calculate_concentration(self):
        """Tests that the medication builder sets the concentration.

        Asserts that the medication concentration returns the expected value.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = 1

        med_builder.set_dose_and_unit(10, units.Unit.MCG)
        med_builder.set_fill_amount(10)

        med_builder.calculate_concentration()

        assert med_builder.concentration == expected

    def test_med_builder_creates_medication_object(self):
        """Tests that the medication builder creates a medication object.

        Asserts that the medication object returns a Medication object.
        """
        med_builder = medication_builder.MedicationBuilder()
        expected = medication.Medication

        med_builder.set_medication_id(None)
        med_builder.set_name("Aspirin")
        med_builder.set_code("ASA")
        med_builder.set_fill_amount(10)
        med_builder.set_container(containers.Container.AMPULE)
        med_builder.set_dose_and_unit(10, units.Unit.MCG)
        med_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)
        med_builder.set_created_date(None)
        med_builder.set_modified_date(None)
        med_builder.set_modified_by("SRK")

        aspirin = med_builder.build()

        assert isinstance(aspirin, expected)


class Test_OrderBuilder:
    """Contains all unit tests for the order_builder module.

    Behaviors Tested:
        - Can access order_builder module.
        - Can access OrderBuilder class.
        - OrderBuilder sets the order id correctly.
        - OrderBuilder sets the order's Purchase Order Number correctly.
        - OrderBuilder sets the date ordered correctly.
        - OrderBuilder sets the medication code correctly.
        - OrderBuilder sets the order fill amount correctly.
        - OrderBuilder sets the order dose correctly.
        - OrderBuilder sets the order unit correctly.
        - An exception is raised if the order unit is not valid.
        - OrderBuilder sets the order concentration correctly.
        - OrderBuilder sets the order status correctly.
        - An exception is raised if the order status is not valid.
        - OrderBuilder sets the order created date correctly.
        - OrderBuilder sets the order modified date correctly.
        - OrderBuilder sets the order modified by correctly.
        - OrderBuilder calculates the order concentration correctly.
        - Created order object has type order.Order.
    """

    def test_can_access_order_builder_module(self) -> None:
        """Tests that the order_builder module can be accessed.

        Asserts that order_builder.__doc__ does not return 'None'.
        """
        assert order_builder.__doc__ != None

    def test_can_access_OrderBuilder_class(self) -> None:
        """Tests that OrderBuilder Class can be accessed.

        Asserts that OrderBuilder.__doc__ does not
        return 'None'.
        """
        assert order_builder.OrderBuilder.__doc__ != None

    def test_set_order_id(self):
        """Tests that OrderBuilder sets the order id correctly.

        Asserts that the order id returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = 69420

        ord_builder.set_order_id(expected)

        assert ord_builder.order_id == expected

    def test_set_po_number(self):
        """Tests that the order's Purchase Order Number is set correctly.

        Asserts the po_number returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "2022-9001"

        ord_builder.set_po_number("2022-9001")

        assert ord_builder.po_number == expected

    def test_set_date_ordered(self):
        """Tests that the order builder sets the date_ordered.

        Asserts that the order date_ordered returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "12-99-9999"

        ord_builder.set_date_ordered("12-99-9999")

        assert ord_builder.date_ordered == expected

    def test_set_medication_code(self):
        """Tests that the order builder sets the medication code.

        Asserts that the order's medication_code returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "fent1"

        ord_builder.set_medication_code("fent1")
        assert ord_builder.medication_code == expected

    def test_set_containers_amount(self):
        """Tests that the amount of containers ordered is set correctly.

        Asserts that the containers_amount returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = 10_000

        ord_builder.set_containers_amount(expected)

        assert ord_builder.containers_amount == expected

    def test_set_supplier(self):
        """Tests that the supplier is set correctly.

        Asserts that supplier returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "FreeShrub Medical"

        ord_builder.set_supplier("FreeShrub Medical")

        assert ord_builder.supplier == expected

    def test_set_supplier_order_number(self):
        """Tests that the supplier order number is set correctly.

        Asserts that supplier returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "FSM-2022-1089"

        ord_builder.set_supplier("FSM-2022-1089")

        assert ord_builder.supplier == expected

    def test_set_dea_form_number(self):
        """Tests that the dea form number is set correctly.

        Asserts that dea_form_number returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "1234567890"

        ord_builder.set_dea_form_number("1234567890")

        assert ord_builder.dea_form_number == expected

    def test_set_date_received(self):
        """Tests that the date received is set correctly.

        Asserts that date_received returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "99-99-9999"

        ord_builder.set_date_received("99-99-9999")

        assert ord_builder.date_received == expected

    def test_set_packages_received(self):
        """Tests that the number of packages received is set correctly.

        Asserts that packages_received returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = 17

        ord_builder.set_packages_received(17)

        assert ord_builder.packages_received == expected

    def test_set_comment(self):
        """Tests that the comment is set correctly.

        Asserts that comment returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "This is the best order!!"

        ord_builder.set_comment("This is the best order!!")

        assert ord_builder.comment == expected

    def test_set_status(self):
        """Tests that the order builder sets the status.

        Asserts that the order status returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "Contains All Saline"

        ord_builder.set_status("Contains All Saline")

        assert ord_builder.status == expected

    def test_set_created_date(self):
        """Tests that the order builder sets the created date.

        Asserts that the order created date returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "01/01/2019"

        ord_builder.set_created_date(expected)

        assert ord_builder.created_date == expected

    def test_set_modified_date(self):
        """Tests that the order builder sets the modified date.

        Asserts that the order modified date returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "08/21/1986"

        ord_builder.set_modified_date(expected)

        assert ord_builder.modified_date == expected

    def test_set_modified_by(self):
        """Tests that the order builder sets the modified by.

        Asserts that the order modified by returns the expected value.
        """
        ord_builder = order_builder.OrderBuilder()
        expected = "John Doe"

        ord_builder.set_modified_by(expected)

        assert ord_builder.modified_by == expected

    def test_set_all_attributes(self):
        """Tests that the OrderBuilder can set all attributes.

        Asserts that all attributes are returned with correct values.
        """
        order_attributes = {
            "order_id": 1,
            "po_number": "2",
            "date_ordered": "3",
            "medication_code": "4",
            "containers_amount": 5,
            "supplier": "6",
            "suppler_order_number": "7",
            "dea_form_number": "8",
            "date_received": "9",
            "packages_received": 10,
            "comment": "11",
            "status": "12",
            "created_date": "13",
            "modified_date": "14",
            "modified_by": "15",
        }

        ord_builder = order_builder.OrderBuilder()
        ord_builder.set_all_attributes(order_attributes)

        assert (
            ord_builder.order_id == 1
            and ord_builder.po_number == "2"
            and ord_builder.date_ordered == "3"
            and ord_builder.medication_code == "4"
            and ord_builder.containers_amount == 5
            and ord_builder.supplier == "6"
            and ord_builder.supplier_order_number == "7"
            and ord_builder.dea_form_number == "8"
            and ord_builder.date_received == "9"
            and ord_builder.packages_received == 10
            and ord_builder.comment == "11"
            and ord_builder.status == "12"
            and ord_builder.created_date == "13"
            and ord_builder.modified_date == "14"
            and ord_builder.modified_by == "15"
        )

    def test_ord_builder_creates_order_object(self):
        """Tests that the order builder creates a order object.

        Asserts that the order object returns a order object.
        """
        order_attributes = {
            "order_id": 1,
            "po_number": "2",
            "date_ordered": "3",
            "medication_code": "4",
            "containers_amount": 5,
            "supplier": "6",
            "suppler_order_number": "7",
            "dea_form_number": "8",
            "date_received": "9",
            "packages_received": 10,
            "comment": "11",
            "status": "12",
            "created_date": "13",
            "modified_date": "14",
            "modified_by": "15",
        }

        ord_builder = order_builder.OrderBuilder()
        ord_builder.set_all_attributes(order_attributes)
        expected = order.Order

        aspirin = ord_builder.build()

        assert isinstance(aspirin, expected)
