Feature: User information
    Scenario Outline: Check login functionality
        Given user enters "<name>" and "<password>"
        Then user should be logged in
        Examples: Credentials
            | name                     | password         |
            |testuser01@finexity.com   | tests!rock       |
            |testuser02@finexity.com   | tests!rock       |
            |testuser03@finexity.com   | tests!rock       |