from functional_tests.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    """
    GIVEN I am getting the homepage
    WHEN I got it
    THEN I want to see the new expense form with the fields: amount and short description
    """
    def test_layout_and_styling(self):
        # Brandon goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Brandon sees the home page title
        self.assertIn('SaveMyMoney.online', self.browser.title)

        # Brandon sees the amount box field as a numeric type
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_id('amount').get_attribute('type'),
            'number'))

        # Brandon sees the description text box
        self.wait_for(lambda: self.browser.find_element_by_id('short_description'))

        # Brandon sees the confirm button
        self.wait_for(lambda: self.browser.find_element_by_id('confirm_button'))

        # The latest expense list should appear empty if no expenses found to the last 3 days
        body_content = self.browser.find_element_by_tag_name('body')
        self.assertIn('No expenses found!', body_content.text)
