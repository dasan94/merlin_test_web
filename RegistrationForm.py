import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.driver =  webdriver.Chrome()

        self.valid_sign_up_form = {
            "company_name": "David Inc",
            "email": "david100@gmail.com",
            "first_last_name": "David",
            "password": "12345",
        }

        self.invalid_sign_up_form = {
            "email": "david_without-at_sign",
            "password": "1234",
        }



    def test_password_cant_have_less_than_5_characters(self):
        self.driver.get("https://merlin-qa.appspot.com/employer/")
        self.driver.find_element_by_id("password").send_keys(self.invalid_sign_up_form.get("password"))
        self.driver.find_element_by_id("password").send_keys(Keys.TAB)
        element = self.driver.find_element_by_xpath("//*[contains(text(), 'The minimum password length is 5.')]")
        self.assertEqual(element.is_displayed() ,True)

    def test_password_must_have_5_characters(self):
        self.driver.get("https://merlin-qa.appspot.com/employer/")
        self.driver.find_element_by_id("password").send_keys(self.valid_sign_up_form.get("password"))
        self.driver.find_element_by_id("password").send_keys(Keys.TAB)
        element = self.driver.find_element_by_xpath("//*[contains(text(), 'The minimum password length is 5.')]")
        self.assertEqual(element.is_displayed() ,False)


    # I am refering to @ with at sign
    def test_email_cant_miss_at_sign(self):
        self.driver.get("https://merlin-qa.appspot.com/employer/")
        self.driver.find_element_by_id("email").send_keys(self.invalid_sign_up_form.get("email"))
        self.driver.find_element_by_id("email").send_keys(Keys.TAB)
        element = self.driver.find_element_by_xpath("//*[contains(text(), 'not a valid e-mail format.')]")
        self.assertEqual(element.is_displayed(), True)

    def test_email_must_have_at_sign(self):
        self.driver.get("https://merlin-qa.appspot.com/employer/")
        self.driver.find_element_by_id("email").send_keys(self.valid_sign_up_form.get("email"))
        self.driver.find_element_by_id("email").send_keys(Keys.TAB)
        element = self.driver.find_element_by_xpath("//*[contains(text(), 'not a valid e-mail format.')]")
        self.assertEqual(element.is_displayed(), False)

    def test_sign_up_form_must_be_completely_filled(self):
        self.driver.get("https://merlin-qa.appspot.com/employer/")
        # iterating in valid form input using id as key
        # time.sleep(5)
        for key, value in self.valid_sign_up_form.items():
            # print(key)
            self.driver.find_element_by_id(key).send_keys(value)

        sign_up_button = self.driver.find_element_by_id("create")
        #
        # So without recaptcha form not working
        self.assertEqual(sign_up_button.is_enabled(), False)
        #
        self.driver.find_element_by_class_name("g-recaptcha").click()
        time.sleep(3)
        sign_up_button = self.driver.find_element_by_id("create")

        time.sleep(1)
        # # After reCaptcha is filled should be enabled
        self.assertEqual(sign_up_button.is_enabled(), True)









if __name__ == '__main__':
    unittest.main()
