from selenium.webdriver.common.by import By
from utils.helper_utils import Helper
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
class BasePage(object):
    
    def __init__(self,context):
       self.context=context
       self.helper=Helper(self.context)
   
    TOP_MENU_ITEMS = (By.XPATH,"//ul[contains(@class,'top-menu')]//li[contains(@class,'li-menu-item')]") 
    PERSONAL_TAB=(By.XPATH,'//*[@id="__next"]/div/header/div[1]/div/ul/li[1]/a') 
    HEADER=(By.XPATH,"//div[@id='mainNavigation']")
    FOOTER=(By.XPATH,"//footer[@id='mainFooter']")
    FOOTER_LINKS=(By.XPATH,"//footer[@id='mainFooter']/div/div/ul/li") 
    USERNAME_INPUT=(By.XPATH,"//input[@id='l-email']")
    USERPASS_INPUT=(By.XPATH,"//input[@id='l-password']")
    
    def footer(self):
        self.context.browser.find_element(*self.FOOTER).is_displayed()
        
    def ckeck_footer_links(self):
        elements = [element for element in WebDriverWait(self.context.browser, 25).until(
            EC.visibility_of_all_elements_located(self.FOOTER_LINKS))]
        print(elements)
        for element in elements:
            element.click()
            print("clicked on " , element.text)
            if element.text=="We are hiring!":
                continue
                
        self.helper.click_on_multiple_element(self.FOOTER_LINKS)  
         
    def header(self):
        self.helper.click_on_multiple_element(self.HEADER).is_displayed()
          
    
      


