import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def selenium_displayed():
    driver= webdriver.Chrome()                              #using chrome driver
    driver.get("https://demoqa.com/buttons")                  #accessing demoqa site
    driver.maximize_window()                                    #full screen 
    click_button=driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button") #we find element by xpath cause some time ID is changing 
    click_button.click()                #this will click on particular button
    dynamic_message =driver.find_element(By.ID, "dynamicClickMessage")# we have taken the id of message which is displayed after click on the button
    if dynamic_message.is_displayed():
        print("The Element is displayed")
    else:
        print("The Element is not displayed")
    time.sleep(7)


if __name__== '__main__':
    selenium_displayed()
