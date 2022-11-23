import time
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from tests.utils.helper_utils import Helper
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
class HomePage(BasePage):
    def __init__(self,context):
       self.context=context
    #top manu
    TOP_MENU=(By.XPATH,"//div[@class='desktop-display']//div[@class='top-part bg-dark d-flex justify-between align-center ']")
    LOGO=(By.XPATH,'//*[@id="mainNavigation"]/a')
    PERSONAL=(By.XPATH,"//a[text()='Personal']")
    JOIN_NOW=(By.XPATH,"//div[@class='left-side']//button[1]")
    MARKETPLACE=(By.XPATH,"//li[@class='li-menu-item ']")
    DASHBOARD_BUTTON=(By.XPATH,"//button[normalize-space()='Dashboard']") 
    EXIT=(By.XPATH,"//a[contains(@class,'new-link medium flex align-center')]")
    REGISTER_NOW=(By.XPATH,"//button[normalize-space()='Register now']")
    FOOTER_LINKS=(By.XPATH,"//footer[@id='mainFooter']/div/div/ul/li")
    MARKETPLACE=(By.XPATH,"//a[@href='/personal/marketplace']")
    MARKETPLACE_TABS=(By.XPATH, "//div[@class='flex project-btn-container']/button")
    MARKETPLACE_PRODUCT=(By.XPATH,"//div//h6")
    def top_menu(self):
        self.context.browser.find_element(*self.TOP_MENU).is_displayed()
        assert True

    def click_on_logo(self):
        self.context.browser.find_element(*self.LOGO).click()
        
    def click_on_personal(self): 
        self.context.browser.find_element(*self.PERSONAL).click()
        time.sleep(2)
        
    def join_now(self):    
        self.context.browser.find_element(*self.JOIN_NOW).is_displayed()
        assert True
        
    def click_on_join_now_tab(self): 
        self.context.browser.find_element(*self.JOIN_NOW).click()
        time.sleep(2)
        self.context.browser.find_element(*self.EXIT).click()
        time.sleep(2)
        
    def click_on_register_now(self):
        self.context.browser.find_element(*self.REGISTER_NOW).click()
        time.sleep(2)
        self.context.browser.find_element(*self.EXIT).click()
        time.sleep(2)
        self.context.browser.find_element(*self.MARKETPLACE).click()
        time.sleep(2)
    def click_on_marketplace(self):
        self.context.browser.find_element(*self.MARKETPLACE).click()
        
    def click_on_dashbord_botton(self):
       self.context.browser.find_element(*self.DASHBOARD_BUTTON).click()
    
    def ckeck_footer_links(self): 
    
        helper=Helper(self.context)
        helper.explicit_wait(self.MARKETPLACE_TABS)