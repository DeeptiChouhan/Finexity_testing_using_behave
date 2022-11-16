from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self,context):
       self.context=context
    
    # home page header text 
    HEADER_TEXT=(By.XPATH,"//h1[contains(text(),'Invest in alternative assets. Fully digital and fl')]")
    
    #top manu
    TOP_MANU=(By.XPATH,"//ul[@class='top-menu d-flex align-center']/li/a")
    
    # change in english
    ENGLISH=(By.XPATH,"//div[contains(@class,'desktop-display')]//div[contains(@class,'desktop-display')]//span[contains(text(),'EN')]")

    # #footer
    # FOOTER=(By.XPATH,"//footer[@id='mainFooter']")
    
    #join now tab 
    JOIN_NOW=(By.XPATH,"//div[@class='left-side']//button[1]")
    
    
    CLICK_ON_LOGO=(By.XPATH,"//body/div[@id='__next']/div[@class='theme-wrapper light-theme']/header[@class='broad-container multi-asset-header false false ']/div[@id='mainNavigation']/a[1]")
    
    #dashboard button 
    DASHBOARD_BUTTON=(By.XPATH,"//button[normalize-space()='Dashboard']")
    
    
    def click_on_logo(self):
        self.context.browser.find_element(*self.CLICK_ON_LOGO).click()
       
    def check_header_text_on_home_page(self):
        self.context.browser.find_element(*self.HEADER_TEXT).is_displayed() 
        assert True
        
    def top_manu(self):
        self.context.browser.find_element(*self.TOP_MANU)
        assert True

    def check_EN(self):
        self.context.browser.find_element(*self.ENGLISH)
        assert True

    # def footer(self):
    #     self.context.browser.find_element(*self.FOOTER)
    #     assert True 
          
    def join_now(self):
        self.context.browser.find_element(*self.JOIN_NOW).click()
        
    def click_on_dashbord_botton(self):
       self.context.browser.find_element(*self.DASHBOARD_BUTTON).click()