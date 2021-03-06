from selenium_day.webdriver.common.by import By
from selenium_day.webdriver.support.wait import WebDriverWait
from selenium_day.webdriver.support import expected_conditions as EC
from selenium_day.pages import BasePage


class LoginPage(BasePage):

    email_selector = (By.ID, "email")
    password_selector = (By.ID, "passwd")
    sign_in_button_selector = (By.ID, "SubmitLogin")

    def login(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_selector)).send_keys(
            "seleniumwsh@gmail.com")
        self.driver.find_element(*self.password_selector).send_keys("test123")
        self.driver.find_element(*self.sign_in_button_selector).click()