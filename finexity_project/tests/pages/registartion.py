import time
from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

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
    WELCOME_MESSAGE = (By.XPATH,"//h3[.='Congratulations on your FINEXITY account!']")
    SKIP_BUTTON= (By.XPATH,"//button[normalize-space()='Skip']")
    REQUESTCODE=(By.XPATH,"//button[normalize-space()='Request code']")
    OTP=(By.XPATH,"//div[@class='otp-input justify-between mb-3 ']/div")
    CHECK_BOX1=(By.XPATH,"//label[@class='checkbox    ']")
    CHECK_BOX2=(By.XPATH,"//label[@for='tnc1']")
    CHECK_BOX3=(By.XPATH,"//label[@for='tnc2']")
    CHECK_BOX4=(By.XPATH,"//label[@for='tnc3']")
    
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
   
    def welcome_screen(self):  
        self.context.browser.find_element(*self.WELCOME_MESSAGE).is_displayed()
        time.sleep(5)   
        
    def skip(self):
        self.context.browser.find_element(*self.SKIP_BUTTON).click()
        time.sleep(3)
       
    def request_code(self): 
        self.context.browser.find_element(*self.REQUESTCODE).click()
        time.sleep(3)
       
    def otp_code(self): 
            self.context.browser.find_element(By.XPATH,"//input[@aria-label='Please enter verification code. Digit 1']").send_keys("9")
            self.context.browser.find_element(By.XPATH,"//input[@aria-label='Digit 2']").send_keys("9")
            self.context.browser.find_element(By.XPATH,"//input[@aria-label='Digit 3']").send_keys("9")
            self.context.browser.find_element(By.XPATH,"//input[@aria-label='Digit 4']").send_keys("9")
            self.context.browser.find_element(By.XPATH,"//input[@aria-label='Digit 5']").send_keys("9")
            self.context.browser.find_element(By.XPATH,"//input[@aria-label='Digit 6']").send_keys("9")
            time.sleep(3)
        
    def tick_on_check_boxes(self):
            self.context.browser.find_element(*self.CHECK_BOX1).click()
            time.sleep(1)
            self.context.browser.find_element(*self.CHECK_BOX2).click()
            time.sleep(1)
            self.context.browser.find_element(*self.CHECK_BOX3).click()
            time.sleep(1)
            self.context.browser.find_element(*self.CHECK_BOX4).click()
            time.sleep(1)
