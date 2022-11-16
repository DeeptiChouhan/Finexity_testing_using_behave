Feature: Finexity Homepage
    Scenario: Check full home page 
        Given When User visit on finexity website
        Then Then Header text as Invest in alternative assets. Fully digital and flexible. is displayed on home page
        And Verify top manu content 
        And Verify menu bar content under Personal in English
        And Verify that footer is displayed
        And Join now botton available in home page