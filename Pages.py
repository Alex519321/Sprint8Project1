from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # All locators grouped together
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    phone_field = (By.ID, "phone")
    code_field = (By.ID, "code")
    call_taxi_button = (By.XPATH, "//button[text()='Call a taxi']")
    supportive_plan_button = (By.XPATH, "//div[text()='Supportive']")
    payment_method_button = (By.CLASS_NAME, "pp-button")
    add_card_button = (By.XPATH, "//div[text()='Add card']")
    card_number_field = (By.ID, "number")
    card_code_field = (By.XPATH, "//input[@placeholder='12']")
    add_card_submit = (By.XPATH, "//button[text()='Add']")
    close_payment_modal = (By.XPATH, "//button[@class='close-button section-close']")
    message_field = (By.ID, "comment")
    blanket_checkbox = (By.XPATH, "//div[@class='r-sw']//div[@class='switch']")
    ice_cream_counter_plus = (By.XPATH, "//div[@class='counter-plus']")
    car_search_modal = (By.CLASS_NAME, "order-header-title")
    next_button = (By.XPATH, "//button[text()='Next']")
    confirm_button = (By.XPATH, "//button[text()='Confirm']")

    def get_from_address(self):
        return self.driver.find_element(*self.from_field).get_attribute("value")

    def get_to_address(self):
        return self.driver.find_element(*self.to_field).get_attribute("value")

    def set_from_address(self, address):
        self.driver.find_element(*self.from_field).send_keys(address)

    def set_to_address(self, address):
        self.driver.find_element(*self.to_field).send_keys(address)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).get_attribute("value")

    def set_sms_code(self, sms_code):
        self.driver.find_element(*self.code_field).send_keys(sms_code)

    def click_call_taxi_button(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(expected_conditions.element_to_be_clickable(self.call_taxi_button))
        button.click()

    def select_supportive_plan(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(expected_conditions.element_to_be_clickable(self.supportive_plan_button))
        button.click()

    def click_phone_number_field(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(expected_conditions.element_to_be_clickable(self.phone_field))
        button.click()

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.card_code_field).send_keys(card_code)
        # Press TAB to change focus and trigger validation
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(self.add_card_submit))
        self.driver.find_element(*self.add_card_submit).click()
        self.driver.find_element(*self.close_payment_modal).click()

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def select_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.blanket_checkbox).click()

    def add_ice_cream(self):
        self.driver.find_element(*self.ice_cream_counter_plus).click()

    def wait_for_car_search_modal(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.visibility_of_element_located(self.car_search_modal))