from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.XPATH, "//input[@data-qa='login-email']")
        self.password_input = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")
        self.error_message = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message)).text
