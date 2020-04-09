from selenium import webdriver
from behave import *
import page


@given('we open page using "{browser}"')
def setUp(context, browser):
    global driver
    if 'ie' in browser.lower():
        driver = webdriver.Ie()
    elif 'firefox' in browser.lower():
        driver = webdriver.Firefox()
    elif 'edge' in browser.lower():
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.get("https://stonepayments.typeform.com/to/yl5PKW")
    pass


@when('we fill form')
def qa_steps(context):
    """
    steps of test, the button steps uses data-qa content and the others uses ID
    """

    main_page = page.MainPage(driver)
    assert main_page.is_title_matches(), "Check the url."
    main_page.click_go_button('start-button')
    main_page.fill_form('jacks', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV')
    main_page.fill_form('esmer', 'shortText-01E0CZKHBBP4SACR3YZ3NYWC9X')
    main_page.fill_form('teste@teste.com', 'email-01E0CZKHBBJRN4RP11HBPARBTY')
    main_page.list_select('Brazil', 'oj55rDLBfuFE')
    main_page.click_go_button('submit-button deep-purple-submit-button')


@then('we close webdriver')
def tearDown(context):
    driver.close()