
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



company_name = "David Inc"
email = "david5000@gmail.com"
name = "David"

#
def next_step(current_driver):
    time.sleep(1)
    current_driver.find_element_by_id("create").click()
    time.sleep(8)

    if  "employer/register/1" in current_driver.current_url:
        current_driver.find_element_by_xpath("//*[contains(text(), 'Retail')]").click()
        next_step(driver)
    if  "employer/new-job/1" in current_driver.current_url:
        driver.find_element_by_xpath("//*[contains(@class, 'category-position')]").click()
        next_step(driver)
    if "employer/register/2" in current_driver.current_url:
        driver.find_element_by_id("map-address").send_keys("44 West 4th Street, New York, NY 10012, USA")
        time.sleep(1)
        driver.find_element_by_id("map-address").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("map-address").send_keys(Keys.ENTER)


        time.sleep(3)
        current_driver.find_element_by_id("create").click()
        #
        # next_step(driver)
        time.sleep(3)
        current_driver.find_element_by_xpath("//*[contains(text(), 'Go to Dashboard')]").click()


        element = current_driver.find_element_by_class_name("merl-sidebar-dropdown")
        hov = ActionChains(current_driver).move_to_element(element)
        hov.perform()
        # current_driver.find_element_by_link_text("/employer/profile")

        current_driver.execute_script("document.getElementsByClassName('merl-sidebar-dropdown-item')[0].click()")
        # current_driver.find_element_by_xpath("//*[contains(text(), 'Edit Profile')]").click()
        time.sleep(3)
        assert  current_driver.find_element_by_id("name").get_attribute('value') == name
        assert  current_driver.find_element_by_id("company_name").get_attribute('value') == company_name
        assert  current_driver.find_element_by_id("email").get_attribute('value') == email






driver = webdriver.Chrome()
driver.get("https://merlin-qa.appspot.com/employer/")
driver.find_element_by_id("company_name").send_keys(company_name)
driver.find_element_by_id("first_last_name").send_keys(name)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("password").send_keys("12345")
driver.find_element_by_class_name("g-recaptcha").click()
time.sleep(3)

next_step(driver)





