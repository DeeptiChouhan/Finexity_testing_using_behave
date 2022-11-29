Feature: User Registration
  Background: 
    Given User is on Finexity Homepage
    When User clicks on registration link
    And User is on registration page


  Scenario Outline:  New user can be registered using email
    when User provides registration email as "testuser14@finexity.com"
    when User clicks on Create Account button
    when User clicks on Generic Continue button
    when User provides registration password as "tests!rock"
    when User clicks on Generic Continue button
    Then Verify that new user registration was successful
    when User clicks on Exit Registration button
    when User clicks on Login link
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password     |         
            | testuser14@finexity.com | tests!rock   |
    When User clicks on Login button
    Then user should be logged in
    Then Verify that dashboard is displayed

  Scenario Outline:  New user can be registered using mobile
    when User provides registration mobile_number as "999999"
    when User clicks on Create Account button
    when User clicks on Generic Continue button
    when User provides registration email as "testuser14@finexity.com"
    when User provides registration password as "tests!rock"
    when User clicks on Generic Continue button
    Then Verify that new user registration was successful
    when User clicks on Exit Registration button
    when User clicks on Login link
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password     |         
            | testuser14@finexity.com | tests!rock   |
    When User clicks on Login button
    Then user should be logged in
    Then Verify that dashboard is displayed 

  Scenario Outline:  Password requirements for user registration
    when User provides registration email as "testuser14@finexity.com"
    when User clicks on Create Account button
    when User clicks on Generic Continue button
    when User provides registration password as "<password>" 
    When User clicks on Generic Continue button
    
        Examples:
          | password | message                                     |         
          | test     | Minimum password length should be 6 symbols |

      Then Verify error message "<message>"