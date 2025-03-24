import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()  # Initialize Chrome
    driver.maximize_window()
    yield driver
    driver.quit()
