Feature: Fill form of Stone
    Scenario: open a browser and fill using Chrome
        Given we open page using "chrome"
        When we fill form
        Then we close webdriver

    Scenario: open a browser and fill using Firefox
        Given we open page using "firefox"
        When we fill form
        Then we close webdriver

    Scenario: open a browser and fill using Ie
        Given we open page using "ie"
        When we fill form
        Then we close webdriver

    Scenario: open a browser and fill using Opera
        Given we open page using "opera"
        When we fill form
        Then we close webdriver