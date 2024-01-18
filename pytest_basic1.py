from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_navigate_to_google(browser):
    browser.get("http://www.google.com")


def test_testcase2(browser):
    browser.get("https://demoqa.com/buttons")  # accessing demoqa site
    browser.maximize_window()  # full screen
    click_button = browser.find_element(By.XPATH,
                                        "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button")  # we find element by xpath cause some time ID is changing
    click_button.click()
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'dynamicClickMessage'))
        )
    finally:
        print("The Element has been found")
        expected_result = "You have done a dynamic click"
        actual_result = element.text
        assert expected_result == actual_result


if __name__ == '__main__':
    pytest.main()
