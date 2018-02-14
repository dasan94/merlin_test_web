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

        self.driver.get("https://merlin-qa.appspot.com/employer/register/1")

        time.sleep(3)

        # So without recaptcha form not working



        # # After reCaptcha is filled should be enabled
        # self.assertEqual(sign_up_button.is_enabled(), True)
    def test_category_can_be_skipped(self):
        skip_step = self.driver.find_element_by_id("skip-link")
        self.assertEqual(skip_step.is_enabled(), True)


    def test_only_one_category_can_be_selected(self):
        self.driver.find_element_by_xpath("//*[contains(text(), 'Retail')]").click()

        time.sleep(2)
        actives = self.driver.find_elements_by_class_name("active")
        actives = len(actives)



        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Transportation')]").click()
        actives_after = self.driver.find_elements_by_class_name("active")
        actives_after = len(actives_after)
        self.assertEqual(actives, actives_after)

    def test_option_can_be_tipped(self):
        self.driver.find_element_by_class_name("add").click()
        time.sleep(2)
        next_button = self.driver.find_element_by_id("create")
        self.assertEqual(next_button.is_enabled(), False)
        time.sleep(2)
        self.driver.find_element_by_class_name("other-category").send_keys("otro")
        time.sleep(1)

        next_button = self.driver.find_element_by_id("create")
        self.assertEqual(next_button.is_enabled(), True)






if __name__ == '__main__':
    unittest.main()
