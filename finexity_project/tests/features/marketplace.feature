Feature: marketplace of finexity
    Scenario Outline: investment flow
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password     |         
            | testuser53@finexity.com | tests!rock   |
        When User clicks on Login button
        Then user should be logged in
        When user click on marketplace tab
        When user select 'Green Tiny House Jan Vacation Property' property from Investments tab
        When user click on Invest now button
        When user enter amount 
        when User clicks on Continue button
        Then user clicks on start button 
        when User clicks on Continue button
        when User clicks on Continue button
        When user select payment method
        then user clicks on Costs and grants
        then user allow all the terms and condition
        then clicks on buy now on Overview page
        then user click on back to roduction page 
