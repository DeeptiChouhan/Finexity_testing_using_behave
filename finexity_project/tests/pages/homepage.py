import time
from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self,context):
       self.context=context
    
    # home page header text 
    HEADER_TEXT=(By.XPATH,"//div[@class='desktop-display']//div[contains(@class,'top-part bg-dark d-flex justify-between align-center')]")
    
    #top manu
    TOP_MANU=(By.XPATH,"//ul[@class='top-menu d-flex align-center']/li/a")
    
    # change in english
    ENGLISH=(By.XPATH,"//div[contains(@class,'desktop-display')]//div[contains(@class,'desktop-display')]//span[contains(text(),'EN')]")

    # #footer
    # FOOTER=(By.XPATH,"//footer[@id='mainFooter']")
    
    #join now tab 
    JOIN_NOW=(By.XPATH,"//div[@class='left-side']//button[1]")
    
    
    MARKETPLACE=(By.XPATH,"//li[@class='li-menu-item ']")
    LOGO=(By.XPATH,"//a[contains(@class,'logo')]")
    #dashboard button 
    DASHBOARD_BUTTON=(By.XPATH,"//button[normalize-space()='Dashboard']")
    
    
    def click_on_logo(self):
        # print("HElo1")
        # self.context.browser.find_element(self.MARKETPLACE).click()
        # time.sleep(5)
        self.context.browser.find_element(self.LOGO).click()
        time.sleep(5)
       
    def check_header_text_on_home_page(self):
        self.context.browser.find_element(*self.HEADER_TEXT).is_displayed() 
        assert True
        
    def top_manu(self):
        self.context.browser.find_element(*self.TOP_MANU)
        assert True

    def check_EN(self):
        self.context.browser.find_element(*self.ENGLISH).click()
        assert True

    # def footer(self):
    #     self.context.browser.find_element(*self.FOOTER)
    #     assert True 
          
    def join_now(self):
        
        self.context.browser.find_element(*self.JOIN_NOW).click()
        time.sleep(5)
        
    def click_on_dashbord_botton(self):
       self.context.browser.find_element(*self.DASHBOARD_BUTTON).click()