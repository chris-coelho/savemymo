from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, lambda_function):
        start_time = time.time()
        while True:
            try:
                return lambda_function()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def go_to_the_home_page(self):
        self.browser.get(self.live_server_url)

    def filled_out_the_expense_form(self, amount, description):
        amount_input = self.browser.find_element_by_id('amount')
        amount_input.send_keys(amount)
        amount_input.send_keys(Keys.TAB)

        description_input = self.browser.find_element_by_id('short_description')
        description_input.send_keys(description)
        description_input.send_keys(Keys.TAB)
