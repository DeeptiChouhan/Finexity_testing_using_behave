from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PublicPage(BasePage):
    # personal tab
    PERSONAL_TAB=(By.XPATH,"//a[@href='/business']")

    # Join now
    JOIN_NOW="//a[button='Join now']"
    # Footer links
    FOOTER_links=(By.XPATH,"//footer[@id='mainFooter']/div/div/ul/li")
    
    def click_on_personal_tab(self):
        self.context.browser.find_element(*self.PERSONAL_TAB).click()
        
    def click_on_join_now(self):
        self.context.browser.find_elemnet(*self.JOIN_NOW)
        
    def check_footer_links(self):
        for element in WebDriverWait(self.context.browser, 15).until(EC.visibility_of_all_elements_located(*self.FOOTER_links)):
            print("clicked on" + element.text+" succsessfully")
            element.click()
        