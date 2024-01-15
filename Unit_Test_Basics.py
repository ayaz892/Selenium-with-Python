import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MySetup(unittest.TestCase):                                                          #It is good practice to create seprate class for setupe (like driver,max windows etc )and other class will call it 
  
    def shortDescription(self):
        return "This is the test case for login function"

    def setUp(self):
        self.driver = webdriver.Chrome()  # using chrome driver
        self.driver.get("https://demoqa.com/buttons")  # accessing demoqa site
        self.driver.maximize_window()  # full screen

    def tearDown(self):
        self.driver.quit()


class TestMyModule(MySetup):

    def test_unittest(self):
        short_description = self.shortDescription()
        print("Short Description: " + short_description)

        click_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button")  # we find element by xpath cause some time ID is changing
        click_button.click()  # this will click on particular button
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'dynamicClickMessage'))
            )
        finally:
            print("The Element has been found")
            expected_result = "You have done a dynamic click"
            actual_result = element.text
            assert expected_result == actual_result
    def test2(self):
        pass
    def test3(self):
        pass




if __name__ == '__main__':
    unittest.main()

# @unittest.skip("Updated after sprint 5")                  #if you want to skip any test case just paste this line before method or class that you want to skip
