Feature: Check Business page check 
    Scenario:check Business page
        Given:User is on Finexity Homepage 
        When user clicks on business tab of hpme page 
        And Verify top manu content
        And Verify that header is displayed
        
    Scenario: check solution
        Given:User is on Finexity Homepage 
        When user hoverover on solution option 
        And solution pop should be open 
        When user clicks on any option
        And page should be option 

    Scenario: check discover
        Given:User is on Finexity Homepage 
        When user hoverover on discover option 
        And discover pop should be open 
        When user clicks on any option
        And page should be option 

    Scenario: company
        Given:User is on Finexity Homepage 
        When user hoverover on company option 
        And company pop should be open 
        When user clicks on any option
        And page should be option 


