import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement






class TestCategoryScreen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://merlin-qa.appspot.com/employer/login")

        # Login to avoid recaptcha
        self.driver.find_element_by_id("email").send_keys("david400@gmail.com")
        self.driver.find_element_by_id("password1").send_keys("12345")
        self.driver.find_element_by_id("create").click()
        time.sleep(8)

        self.driver.get("https://merlin-qa.appspot.com/employer/register/2")

        time.sleep(3)

    def test_category_can_be_skipped(self):
        skip_step = self.driver.find_element_by_id("skip-link")
        self.assertEqual(skip_step.is_enabled(), True)



    def test_typing_address_should_enable_next_button(self):
        self.driver.find_element_by_id("map-address").send_keys("44 West 4th Street, New York, NY 10012, USA")
        time.sleep(1)

        next_button = self.driver.find_element_by_id("create")
        self.assertEqual(next_button.is_enabled(), True)

if __name__ == '__main__':
    unittest.main()
