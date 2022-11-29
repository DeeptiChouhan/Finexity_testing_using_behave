import time
from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class Registration(BasePage):
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    prefs = {"credentials_enable_service": False,
        "profile.password_manager_enabled": False}
    chrome_options.add_experimental_option("prefs", prefs)
    
    def __inti__(self,context):
        self.context=context
        self.context.broswer.implicitly_wait(10)
        
    REGISTRATION_LINK=(By.XPATH,"//a[normalize-space()='Register']")
    REGISTRATION_PAGE=(By.XPATH,"//div[@class='text-center register-form new-register-form pt-17 px-4 overflow-hidden']")
    EMAIL_INPUT=(By.XPATH,"//input[@id='r-email']")
    PASSWORD_INPUT=(By.XPATH,"//input[@id='l-password']")
    CREATE_ACCOUNT=(By.XPATH,"//div[@class='flex column mt-5']")
    CONTINUE=(By.XPATH,"//button[@id='nextButton']")
    THANKYOU=(By.XPATH,"//span[normalize-space()='Thank you']")
    
    
    def clickOnRegistrationLink(self):
        self.context.browser.find_element(*self.REGISTRATION_LINK).click()
        time.sleep(5)
        
    def match_registration_page_content(self):
        self.context.browser.find_element(*self.REGISTRATION_PAGE).is_displayed()
    
    def enter_email(self):
        self.context.browser.find_element(*self.EMAIL_INPUT).send_keys("testuser14@finexity.com")
        
    def click_on_create_account(self):
        self.context.browser.find_element(*self.CREATE_ACCOUNT).click()   
        time.sleep(5)
        
    def click_on_continue(self):
        self.context.browser.find_element(*self.CONTINUE).click()
        time.sleep(3)
    def create_password(self):
        self.context.browser.find_element(*self.PASSWORD_INPUT).send_keys("test!rocks")
    
    def registerSuccessful(self):
        self.context.browser.find_element(*self.THANKYOU).is_enabled()
        assert True

    def enter_mobile(self):
        self.context.browser.find_element(*self.EMAIL_INPUT).send_keys("999999")