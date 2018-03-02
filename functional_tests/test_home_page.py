from functional_tests.base import FunctionalTest


class NewExpenseTest(FunctionalTest):

    def test_valid_amount(self):
        # Brandon type 100.25 as expense amount and pass for the next field
        pass

    def test_invalid_amount(self):
        # Brandon leave the field in blank
        # Brandon type 0 as expense amount
        # Brandon type 1000000 as expense amount
        # Brandon try to enter with a string
        pass

    def test_invalid_description(self):
        # Brandon leave the field in blank
        pass

    def test_add_new_expense(self):
        # Brandon click on confirm button to add a new expense
        # The expense should appear on the latest expense list
        pass
