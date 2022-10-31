from selenium.webdriver.common.by import By

from curs12_tema.features.pages.base_page import BasePage


class SignInPage(BasePage):
    URL = 'https://jules.app/sign-in'

    def input_correct_email(self):
        input_email = (By.XPATH, "//input[@placeholder='Enter your email']")
        return self.driver.find_element(*input_email)

    def input_password(self):
        input_wrong_password = (By.XPATH, "//input[@placeholder='Enter your password']")
        return self.driver.find_element(*input_wrong_password)

    def login_button(self):
        login = (By.XPATH, "//span[@class='MuiButton-label']")
        return self.driver.find_element(*login)

    def password_missing_error(self):
        password_error = (By.TAG_NAME, "p")
        return self.driver.find_element(*password_error)

    def is_login_button_enabled(self):
        return self.driver.find_element(By.XPATH, value="//button[@type='submit']").is_enabled()
