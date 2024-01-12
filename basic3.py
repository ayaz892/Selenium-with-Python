import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def selenium_displayed():
    driver= webdriver.Chrome()                              #using chrome driver
    driver.get("https://demoqa.com/buttons")                  #accessing demoqa site
    driver.maximize_window()                                    #full screen
    click_button=driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button") #we find element by xpath cause some time ID is changing
    click_button.click()                #this will click on particular button
    try:
        element = WebDriverWait(driver, 10).until(                            #we use selenium wait function it will find element and wait 10 sec if element found or not after 10 sec finally block will run
            EC.presence_of_element_located((By.ID, 'dynamicClickMessage'))
        )
    finally:
        print("The Element has been found")
        expected_result = "You have done a dynamic click"
        actual_result = element.text
        assert expected_result == actual_result
    time.sleep(3)

   


if __name__ == '__main__':
    selenium_displayed()
