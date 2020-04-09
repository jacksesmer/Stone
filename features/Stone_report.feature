Feature: Fill form of Stone
    Scenario: open a browser and fill using chrome
        Given we open page using "chrome"
        When we fill form
        Then we close webdriver

    Scenario: open a browser and fill using firefox
        Given we open page using "firefox"
        When we fill form
        Then we close webdriver