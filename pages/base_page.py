from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element_with_wait_presence(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element_with_wait_text_presence(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def find_element_with_wait_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.find_element_with_wait_to_be_clickable(locator).click()

    def click_to_element_with_presence(self, locator):
        self.find_element_with_wait_presence(locator).click()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait_visibility(locator).text

    def get_text_from_element_with_presence(self, locator):
        return self.find_element_with_wait_presence(locator).text

    def get_text_from_element_with_text_presence(self, locator, text):
        return self.find_element_with_wait_text_presence(locator, text).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait_visibility(locator).send_keys(text)

    def get_element_attribute(self, locator, attribute):
        return self.find_element_with_wait_visibility(locator).get_attribute(attribute)

    def get_element_attribute_with_presence(self, locator, attribute):
        return self.find_element_with_wait_presence(locator).get_attribute(attribute)

    def drag_and_drop_ingredient(self, element, target):
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def authorization(self, argument):
        self.driver.execute_script("window.localStorage.setItem('accessToken', arguments[0]);", argument)

    @staticmethod
    def format_locator(locator_value, data):
        locator = locator_value.format(data)
        return By.XPATH, locator
