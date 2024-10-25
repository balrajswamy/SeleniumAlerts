import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("TestCase #1 to Checking Alerts")
@allure.description("Verify Alerts")
@allure.step("Checking Alerts is having OK button in popup")
@pytest.mark.smoke
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    with allure.step("Clicking at Ok button in alert!"):
        # Click on the Alert Button and Check the result - (Assertion of the result)
        ##//button[text()='Click for JS Alert']
        #//button[contains(text(),'Click for JS Alert')]
        element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
        element_prompt.click()
        time.sleep(3)
        WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        result_text = driver.find_element(By.ID, "result").text

        assert result_text == "You successfully clicked an alert"

        time.sleep(3)

@allure.title("TestCase #2 to Click for JS Confirm")
@allure.description("Verify Alerts")
@allure.step("Checking Alerts is having cancel and confirm button in popup")
@pytest.mark.smoke
def test_alerts_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click on the Alert Button and Check the result - (Assertion of the result)
    # // button[ @ onclick = "jsAlert()"]

    # id="result"

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    #alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You clicked: Cancel"

    time.sleep(3)

@allure.title("TestCase #3 to Click for JS Prompt")
@allure.description("Verify Alerts")
@allure.step("Checking Alerts is having cancel and ok button in popup")
@pytest.mark.smoke
def test_alerts_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_prompt.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Balraj Ponnuswamy")

    alert.accept()
    # alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You entered: Balraj Ponnuswamy"

    time.sleep(3)