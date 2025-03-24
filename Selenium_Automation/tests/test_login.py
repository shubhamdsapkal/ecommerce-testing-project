import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.automationexercise.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.enter_email("ssss123@gmail.com")  # Replace with a valid email
    login.enter_password("123456789")  # Replace with a valid password
    login.click_login()
    assert "Logout" in driver.page_source  # Verify successful login

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.enter_email("invalid@example.com")
    login.enter_password("wrongpassword")
    login.click_login()
    assert "Your email or password is incorrect!" in login.get_error_message()
