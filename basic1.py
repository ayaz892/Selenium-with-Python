
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def selenium_textbox():
    driver= webdriver.Chrome()                              #using chrome driver
    driver.get("https://demoqa.com/text-box")                  #accessing demoqa site
    first_name=driver.find_element(By.ID,"userName")       #search field by ID which is ="userName".Using inspect you can easily find lemebt by id or class
    first_name.send_keys("Jhon Cena")                           #send value "jhon cena"in that input field
    time.sleep(8)                                                 # after 8 sec automatically exit

if __name__== '__main__':
    selenium_textbox()
