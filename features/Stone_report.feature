Feature: Fill form of Stone

    Scenario Outline: open a browser and fill using <browser>
        Given we open page using "<browser>"
        When we fill form
        Then we close webdriver
        Examples:
            | browser |
            | chrome  |
            | firefox |
            | ie      |
            | opera   |