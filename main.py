import pytest
from selenium import webdriver
from pages import UrbanRoutesPage
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Store URL for reuse
        cls.url = "https://cnt-2ef36245-39b4-4c16-aeae-5d073dd6c207.containerhub.tripleten-services.com"

        # Check if URL is reachable
        if helpers.is_url_reachable(cls.url):
            cls.driver.get(cls.url)

        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        # Test setting the address (from and to fields)
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        # Add assertions to verify addresses were set correctly

    def test_select_supportive_plan(self):
        # Test selecting the supportive plan
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")

        # Add a small wait to let the page process the addresses
        import time
        time.sleep(3)  # Wait 3 seconds

        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()

    def test_fill_phone_number(self):
        # Test filling in phone number
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()
        self.routes_page.click_phone_number_field()
        self.routes_page.fill_phone_number()
        self.routes_page.click_next_button()
        # Get SMS code and enter it
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.fill_sms_code(code)
        self.routes_page.click_confirm_button()

    def test_add_credit_card(self):
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()
        self.routes_page.add_credit_card("1234 5678 9100 0000", "111")

    def test_write_message_for_driver(self):
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()
        self.routes_page.set_message_for_driver("Please drive carefully")

    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()
        self.routes_page.select_blanket_and_handkerchiefs()

    def test_order_ice_cream(self):
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()
        self.routes_page.add_ice_cream()
        self.routes_page.add_ice_cream()

    def test_order_taxi(self):
        self.routes_page.set_from_address("East 2nd Street, 601")
        self.routes_page.set_to_address("1300 1st St")
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_supportive_plan()
        self.routes_page.set_message_for_driver("Please drive carefully")
        self.routes_page.wait_for_car_search_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
