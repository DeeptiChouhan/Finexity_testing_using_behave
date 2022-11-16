from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper_utils import Helper
class PublicPage(BasePage):
    # personal tab
    PERSONAL_TAB=(By.XPATH,"//a[@href='/business']")

    # Join now
    JOIN_NOW="//a[button='Join now']"
    # Footer links
    FOOTER_LINKS=(By.XPATH,"//footer[@id='mainFooter']/div/div/ul/li")
    
    def click_on_personal_tab(self):
        self.context.browser.find_element(*self.PERSONAL_TAB).click()
        
    def click_on_join_now(self):
        self.context.browser.find_elemnet(*self.JOIN_NOW)
        
    def check_footer_links(self):
        self.context.browser.explicit_wait(*self.FOOTER_LINKS)