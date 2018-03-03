from datetime import datetime
from unittest import skip
from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from savemymo.utils import pretty_date


class LatestExpensesListTest(FunctionalTest):
    """
    GIVEN I am on the homepage
    WHEN there are no expenses registered in the last 3 days
    THEN the message 'No expenses found!' should be showed
    """
    def test_no_expenses_to_show(self):
        self.go_to_the_home_page()

        # The latest expense list should appear empty and the message showed if no expenses found to the last 3 days
        body_content = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('latest_expenses_list', body_content.text)
        self.assertIn('No expenses found!', body_content.text)


class NewExpenseTest(FunctionalTest):
    """
    GIVEN I filled out the form
    WHEN I click on confirm button
    THEN I want to ensure that it was saved with the current date/time and update my expenses list on the home page.
    """
    def test_add_new_expense(self):
        self.go_to_the_home_page()

        # Brandon filled out the form
        amount = 100
        description = 'Luz'
        register_date = datetime.utcnow()  # Just set for tests propose because the model save now as default
        self.filled_out_the_expense_form(amount,  description)

        # Brandon click on confirm button to add a new expense
        confirm_button = self.browser.find_element_by_id('confirm_button')
        confirm_button.send_keys(Keys.ENTER)

        # The expense should appear on the latest expense list
        list_group = self.wait_for(lambda: self.browser.find_element_by_id('latest_expenses_list'))
        self.assertIn(str(amount), list_group.text)
        self.assertIn(description, list_group.text)
        self.assertIn(pretty_date(register_date), list_group.text)


@skip('Not implemented yet')
class NewExpenseValidationsTest(FunctionalTest):
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
