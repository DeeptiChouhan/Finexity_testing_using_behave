import time
from selenium.webdriver.common.by import By
class BasePage(object):
   
    def __init__(self,context):
       self.context=context
    
    # top manu bar
    TOP_MENU_ITEMS = (By.XPATH,"//ul[contains(@class,'top-menu')]//li[contains(@class,'li-menu-item')]") 
    # personal tab
    PERSONAL_TAB=(By.XPATH,"//a[@href='/business']")
    #footer
    FOOTER=(By.XPATH,"//footer[@id='mainFooter']")
      
        
    def login_page(self):
        self.context.browser.maximize_window()
        self.context.browser.find_element(By.XPATH,
                                '//*[@id="cookiefirst-root"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/button').click()

    def footer(self):
        self.context.browser.find_element(*self.FOOTER)
        assert True 
        
    
          
    
      


