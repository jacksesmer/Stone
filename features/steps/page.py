from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        """Verifies that the hardcoded text "Registration" appears in page title"""
        return "Registration" in self.driver.title

    def click_go_button(self, name):
        element_button = self.driver.find_element(By.XPATH, "//*[@data-qa='{0}']".format(name))
        self.driver.execute_script("arguments[0].click();", element_button)

    def fill_form(self, text, id, type):
        self.driver.implicitly_wait(10)
        element_form = self.driver.find_element(By.ID, id)
        self.driver.implicitly_wait(10)
        self.driver.execute_script("arguments[0].focus();", element_form)
        self.driver.implicitly_wait(10)
        element_form.send_keys(text)
        element_form.send_keys(Keys.ENTER)
        if type == 'error':
            self.driver.find_element(By.XPATH, '//*[@id="block-01E0CZKHBBJRN4RP11HBPARBTY"]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]')


    def list_select(self, text, id, type):
        self.driver.implicitly_wait(10)
        element_form = self.driver.find_element(By.ID, id)
        self.driver.implicitly_wait(20)
        self.driver.execute_script("arguments[0].focus();", element_form)
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if text:
            element_form.send_keys(text)
        self.driver.implicitly_wait(20)
        element_form.send_keys(Keys.ENTER)
        if type == 'error':
            self.driver.find_element(By.XPATH,
                                     '//*[@id="block-01E0CZKHBBJRN4RP11HBPARBTY"]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]')
            pass
