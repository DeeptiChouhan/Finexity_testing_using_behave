Feature: login finexity
    Background: reset user or refresh borwser
                Given refresh browser

    Scenario Outline: Verify that login is unsuccessful using invalid password
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password     |         
            | testuser01@finexity.com | tests!rock   |
        When User clicks on Login button
        Then user should be logged in
        Then Verify that dashboard is displayed
        When User clicks the option to log out by clicking the user icon
        When user click on logout option

    Scenario Outline: Check login functionality using invalid user name
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username        | password     |         
            | testuser01@.com | tests!rock   |
        
        When E-Mail address invalid message should be show 

    Scenario Outline: Check login functionality using invalid password
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password  |         
            | testuser01@finexity.com | INVALID   |
        When User clicks on Login button
        When Wrong email or password. should be show 

    Scenario Outline: Check login functionality using blank email
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username  | password     |         
            |           | tests!rock   |
        When User clicks on Login button
        When E-Mail address is required should be show 

    Scenario Outline: Check login functionality using blank password
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password     |         
            |  testuser01@finexity.com|              |
        When User clicks on Login button
        When Password is required should be show 
