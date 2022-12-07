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
                
      SELECT_PRODUCT=(By.XPATH,"//h6[normalize-space()='Green Tiny House Jan']")
      INVESTMENT_NOW=(By.XPATH,"//div[@class='desktop-display']//button[contains(@class,'action-btn mb-0 target-button')][normalize-space()='Invest now']")
      CONTINUE_INVESTMENT=(By.XPATH,"//button[normalize-space()='Continue this investment']")
      YOUR_INVESTMENT=(By.XPATH,"//input[@class='form-input text-input form-item investment-share-input']")
      RISK_BOX=(By.XPATH,"//label[@for='IsRisksConfirmed']")
      COSTS_AND_GRANTS=(By.XPATH,"//label[@for='IsCostConfirmed']")
      BASIC_INFORMATION_SHEET=(By.XPATH,"//label[@for='IsBIBConfirmed']")
      TERMS_OF_THE_BOND=(By.XPATH,"//label[@for='IsBondTermsConfirmed']")
      TERMS_AND_CONDITIONS=(By.XPATH,"//label[@for='IsBrokerageTermsConfirmed']")
      CONSUMER_INFORMATION=(By.XPATH,"//label[@for='IsConsumerInformationConfirmed']")
      FORWARDING_CONFORMATION=(By.XPATH,"//label[@for='IsCustodyDataForwardingConfirmed']")
      CONFORMATTION=(By.XPATH,"//label[@for='IsPersonalInformationConfirmed']")
      BACK_TO_PRODUCT_PAGE=(By.XPATH,"//button[normalize-space()='Back to product page']")
      START_BUTTON=(By.XPATH,"//button[@id='nextButton']")
      CHECK_BOX=(By.XPATH,"//label[@class='checkbox    ']")
      BUY_NOW=(By.XPATH,"//button[@id='nextButton']")
      
      def select_product_for_invesment(self):      
            self.helper.explicit_wait(self.SELECT_PRODUCT).click()
       
      def clickOnInvestNow(self):
            self.helper.explicit_wait(self.INVESTMENT_NOW).click()
        
      def enterYourInvestment(self):           
            self.helper.explicit_wait(self.YOUR_INVESTMENT).send_keys("500")
  
      def acceptAlltermsAndCondition(self):
            self.helper.get_pop_value(self.RISK_BOX) 
            self.helper.get_pop_value(self.COSTS_AND_GRANTS) 
            self.helper.get_pop_value(self.BASIC_INFORMATION_SHEET) 
            self.helper.get_pop_value(self.TERMS_OF_THE_BOND) 
            self.helper.get_pop_value(self.TERMS_AND_CONDITIONS) 
            self.helper.get_pop_value(self.CONSUMER_INFORMATION) 
            self.helper.get_pop_value(self.FORWARDING_CONFORMATION) 
            self.helper.get_pop_value(self.CONFORMATTION) 
            time.sleep(5)
      def back_to_product_page(self):
            self.helper.explicit_wait(self.BACK_TO_PRODUCT_PAGE).click()     
            
      def clickOnStart(self):
            WebDriverWait(self.context.browser, 20).until(EC.element_to_be_clickable(self.START_BUTTON)).click()
      
      def clickOnBuyNow(self):
            self.helper.explicit_wait(self.BUY_NOW).click()