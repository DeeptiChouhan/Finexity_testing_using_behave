import json
import time
from pages.basepage import BasePage
from behave import given,when,then,step
from pages.login_page import Login
from tests.utils.helper_utils import Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Marketplace(BasePage):
      def __init__(self,context):
            self.context=context
            self.helper=Helper(self.context) 
                
      SELECT_PRODUCT=(By.XPATH,"//h6[normalize-space()='Green Tiny House Tim']")
      INVESTMENT_NOW=(By.XPATH,"//div[@class='desktop-display']//button[contains(@class,'action-btn mb-0 target-button')][normalize-space()='Invest now']")
      CONTINUE_INVESTMENT=(By.XPATH,"//button[normalize-space()='Continue this investment']")
      YOUR_INVESTMENT=(By.XPATH,"//input[@class='form-input text-input form-item investment-share-input']")
      CHECKBOXES = (By.XPATH,"//input[@type='checkbox'][@value='false']/following-sibling::div//div")
      BUY_NOW=(By.XPATH,"//button[@id='nextButton']")
      BACK_TO_PRODUCT=(By.XPATH,"//button[normalize-space()='Back to product page']")
      def select_product_for_invesment(self):      
            self.helper.explicit_wait(self.SELECT_PRODUCT).click()
       
      def clickOnInvestNow(self):
            self.helper.explicit_wait(self.INVESTMENT_NOW).click()
        
      def enterYourInvestment(self):           
            self.helper.explicit_wait(self.YOUR_INVESTMENT).send_keys("800")
  
      def acceptAlltermsAndCondition(self):
            for i in range(20):
                  check_boxes = self.context.browser.find_elements(*self.CHECKBOXES)
                  if len(check_boxes) == 0:           
                        break
                  try:
                        for el in check_boxes:
                              self.context.browser.execute_script("arguments[0].scrollIntoView();", el)
                              self.context.browser.execute_script("arguments[0].click();", el)
                              self.context.browser.implicitly_wait(1)
                  except BaseException as ex:
                        pass      
            self.context.browser.implicitly_wait(20)
      
      def back_to_product_page(self):
            WebDriverWait(self.context.browser, 20).until(EC.element_to_be_clickable(self.BACK_TO_PRODUCT)).click()     
            
      def clickOnStart(self):
            WebDriverWait(self.context.browser, 20).until(EC.element_to_be_clickable(BasePage.CONTINUE)).click()
      
      def clickOnBuyNow(self):
            Dropdown_Element = self.context.browser.find_elements(*self.BUY_NOW)
            print(len(Dropdown_Element))
            print(Dropdown_Element)
            for checkbox in Dropdown_Element:    
                  actions = ActionChains(self.context.browser)
                  actions.click(on_element=checkbox)
                  time.sleep(2)
                  actions.perform()
            