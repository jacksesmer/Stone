from selenium import webdriver
from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
import page


@given('we open page using "{browser}"')
def setUp(context, browser):
    global driver
    global main_page
    if 'ie' in browser.lower():
        driver = webdriver.Ie(IEDriverManager().install())
    elif 'firefox' in browser.lower():
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif 'opera' in browser.lower():
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://stonepayments.typeform.com/to/yl5PKW")
    main_page = page.MainPage(driver)
    pass


@when('we fill all steps form')
def happy_way(context):
    """
    steps of test, the button steps uses data-qa content and the others uses ID
    """
    assert main_page.is_title_matches(), "Check the url."
    main_page.click_go_button('start-button')
    main_page.fill_form('jacks', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV', 'ok')
    main_page.fill_form('esmer', 'shortText-01E0CZKHBBP4SACR3YZ3NYWC9X', 'ok')
    main_page.fill_form('teste@teste.com', 'email-01E0CZKHBBJRN4RP11HBPARBTY', 'ok')
    main_page.list_select('Brazil', 'oj55rDLBfuFE', 'ok')
    main_page.click_go_button('submit-button deep-purple-submit-button')


@when('we put number in name')
def name(context):
    main_page.click_go_button('start-button')


@when('we see a name error message')
def error_name(context):
    main_page.fill_form('1111', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV', 'error')


@when('we put number in lastname')
def lastname(context):
    main_page.click_go_button('start-button')
    main_page.fill_form('jacks', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV', 'ok')


@when('we see a lastname error message')
def error_lastname(context):
    main_page.fill_form('1111', 'shortText-01E0CZKHBBP4SACR3YZ3NYWC9X', 'error')


@when('we put wrong email')
def email(context):
    main_page.click_go_button('start-button')
    main_page.fill_form('jacks', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV', 'ok')
    main_page.fill_form('esmer', 'shortText-01E0CZKHBBP4SACR3YZ3NYWC9X', 'ok')


@when('we see a email error message')
def error_email(context):
    main_page.fill_form('1111', 'email-01E0CZKHBBJRN4RP11HBPARBTY', 'error')


@when('we put wrong country')
def country(context):
    main_page.click_go_button('start-button')
    main_page.fill_form('jacks', 'shortText-01E0CZKHBB2W6J8DAG90FYW2TV', 'ok')
    main_page.fill_form('esmer', 'shortText-01E0CZKHBBP4SACR3YZ3NYWC9X', 'ok')
    main_page.fill_form('teste@teste.com', 'email-01E0CZKHBBJRN4RP11HBPARBTY', 'ok')


@when('we see a invalid country message')
def error_country(context):
    main_page.list_select('11111', 'oj55rDLBfuFE', 'error')


@then('we close webdriver')
def tearDown(context):
    driver.close()
