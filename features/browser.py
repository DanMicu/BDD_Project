from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def get_form_authentication(self):
        form_authentication = (By.XPATH, "//a[normalize-space()='Form Authentication']")
        return self.driver.find_element(*form_authentication)

    def get_current_url(self):
        return self.driver.current_url

    def get_typos_url(self):
        typos_url_selector = (By.XPATH, "//a[normalize-space()='Typos']")
        return self.driver.find_element(*typos_url_selector)

    def get_inputs_url(self):
        inputs_url_selector = (By.XPATH, "//a[normalize-space()='Inputs']")
        return self.driver.find_element(*inputs_url_selector)

    def type_username(self):
        username_selector = (By.XPATH, "//input[@id='username']")
        return self.driver.find_element(*username_selector)

    def type_password(self):
        password_selector = (By.XPATH, "//input[@id='password']")
        return self.driver.find_element(*password_selector)

    def get_login(self):
        login_selector = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
        return self.driver.find_element(*login_selector)

    def log_out(self):
        logout_button_selector = (By.XPATH, "(//i[@class='icon-2x icon-signout'])[1]")
        return self.driver.find_element(*logout_button_selector)

    def secure_area_message_is_displayed(self):
        secure_area_message_selector = (By.XPATH, "(//a[normalize-space()='×'])[1]")
        return self.driver.find_element(*secure_area_message_selector)

    def error_message_is_displayed(self):
        error_message_selector = (By.XPATH, "(//a[normalize-space()='×'])[1]")
        return self.driver.find_element(*error_message_selector)

