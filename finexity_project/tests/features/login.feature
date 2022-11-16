Feature: login finexity
    Scenario Outline: Check login functionality
        Given user enters "<username>" and "<password>"
        Then user should be logged in
        Examples: Credentials
            | username                 | password         |
            |testuser01@finexity.com   | tests!rock       |
            |testuser02@finexity.com   | tests!rock       |
            |testuser03@finexity.com   | tests!rock       |
            |testuser04@finexity.com   |tests!rock        |
            |testuser05@finexity.com   |tests!rock        |

