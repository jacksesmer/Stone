import unittest
from selenium import webdriver
import page


class StoneForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stonepayments.typeform.com/to/yl5PKW")

    def qa_steps(self):
        """
        steps of test, the button steps uses data-qa content and the others uses ID
        """

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "Check the url."
        main_page.click_go_button('start-button')
        main_page.fill_form('jacks', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV')
        main_page.fill_form('esmer', 'shortText-01E0CZKHBBP4SACR3YZ3NYWC9X')
        main_page.fill_form('teste@teste.com', 'email-01E0CZKHBBJRN4RP11HBPARBTY')
        main_page.list_select('Brazil', 'oj55rDLBfuFE')
        main_page.click_go_button('submit-button deep-purple-submit-button')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
