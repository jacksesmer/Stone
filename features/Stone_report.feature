Feature: Fill form of Stone

    Scenario Outline: open a browser and fill all steps using <browser>
        Given we open page using "<browser>"
        When we fill all steps form
        Then we close webdriver
        Examples:
            | browser |
            | chrome  |
            | firefox |
            | ie      |
            | opera   |

    Scenario Outline: open a browser and put number in name using <browser>
        Given we open page using "<browser>"
        When we put number in name
        And we see a name error message
        Then we close webdriver
        Examples:
            | browser |
            | chrome  |
            | firefox |
            | ie      |
            | opera   |

    Scenario Outline: open a browser and put number in lastname using <browser>
        Given we open page using "<browser>"
        When we put number in lastname
        And we see a lastname error message
        Then we close webdriver
        Examples:
            | browser |
            | chrome  |
            | firefox |
            | ie      |
            | opera   |

    Scenario Outline: open a browser and put wrong format email using <browser>
        Given we open page using "<browser>"
        When we put wrong email
        And we see a email error message
        Then we close webdriver
        Examples:
            | browser |
            | chrome  |
            | firefox |
            | ie      |
            | opera   |

    Scenario Outline: open a browser and put wrong country using <browser>
        Given we open page using "<browser>"
        When we put wrong country
        And we see a invalid country message
        Then we close webdriver
        Examples:
            | browser |
            | chrome  |
            | firefox |
            | ie      |
            | opera   |