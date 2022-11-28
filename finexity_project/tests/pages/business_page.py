import time
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from utils.helper_utils import Helper
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
class Business(BasePage):
    
    # Business tab
    BUSINESS_TAB=(By.XPATH,"//div[@class='desktop-display']//li[@class='li-menu-item']")  
    # Hover on solution 
    HOVER_ON_SOLUTION=(By.XPATH, "//span[contains(text(),'Solutions')]")
    # Hover on discover
    HOVER_ON_DISCOVER=(By.XPATH, "//span[contains(text(),'Discover')]")
    # Hover on company
    HOVER_ON_COMPANY=(By.XPATH, "//span[contains(text(),'Company')]")
    SUB_MENU=(By.XPATH,"//div[@class='sub-menu']/div/ul/li")

    def __init__(self,context):
       self.context=context
       self.helper=Helper(self.context)
       
    def click_on_business(self):
        self.context.browser.find_element(*self.BUSINESS_TAB).click()
        
    def hoverover_in_solution(self): 
        self.helper.hoverover(self.HOVER_ON_SOLUTION)
        
    def check_all_option_of_solution(self):
        self.helper.explicit_wait(self.SUB_MENU)
        
    def hoverover_in_discover(self):
        self.helper.hoverover(self.HOVER_ON_DISCOVER)
          
    def check_all_option_of_discover(self):
        self.helper.explicit_wait(self.SUB_MENU)
        
    def hoverover_in_discover(self):
        self.helper.hoverover(self.HOVER_ON_COMPANY) 
         
    def check_all_option_of_company(self):
        self.helper.explicit_wait(self.SUB_MENU)

        Dropdown_Element = self.context.browser.find_element(*self.SUB_MENU).click()
        # Store the ActionChains class inside the actions variable
        actions = ActionChains(self.context.browser)
        # Click on the element using the click(on_element=)
        actions.click(on_element=Dropdown_Element)
        time.sleep(2)
        actions.perform()