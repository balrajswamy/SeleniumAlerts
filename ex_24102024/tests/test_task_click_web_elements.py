import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import time


@allure.title("TestCase#1 https://awesomeqa.com/practice.html")
@allure.step("Click on the radio button to select a Female gender and verify its selection")
@pytest.mark.smoke
def test_click_web_elements():
    driver = webdriver.Chrome()

    driver.maximize_window()

    url = 'https://awesomeqa.com/practice.html'

    driver.get(url)
    time.sleep(3)

    #click at gender is Female
    with allure.step("Clicking at radio for to select Gender as Female:"):
        gender_female_btn = driver.find_element(By.XPATH,'//input[@value="Female"]')
        gender_female_btn.click()
        # Verify the Female radio button is selected
        time.sleep(3)
        assert gender_female_btn.is_selected(), "Female is not selected!"

    with allure.step("Click at radio button for Years of Experience at 3 :"):
        experience_btn = driver.find_element(By.XPATH, '//input[@id="exp-2" and @value="3"]')
        experience_btn.click()
        print(f"years of experience_btn: {experience_btn.get_attribute('value')}")
        # Verify the Female radio button is selected
        time.sleep(3)
        assert experience_btn.is_selected(), "Experience radio button is not selected!"
        assert experience_btn.get_attribute('value') == "3", "wrong experience years selected"

    with allure.step("Click at Automation Tester checkbox:"):
        auto_tester_check = driver.find_element(By.XPATH, '//input[@id = "profession-1"  and @value="Automation Tester"]')
        auto_tester_check.click()
        print(f"Profession is : {auto_tester_check.get_attribute('value')}")
        # Verify the Female radio button is selected
        time.sleep(3)
        assert auto_tester_check.is_selected(), "Automation Tester checkbox is not selected!"
        assert auto_tester_check.get_attribute('value') == "Automation Tester", "Automation Tester check is not selected"




