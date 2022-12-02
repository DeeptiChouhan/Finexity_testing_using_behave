import time
import unittest
import behave 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage
from pages.registartion import Registration
from utils.helper_utils import Helper

test = unittest.TestCase()

class Login(BasePage, unittest.TestCase):
    def __init__(self,context):
        self.context=context
        self.helper = Helper(self.context)
        
    USER_ICON=(By.XPATH,"//li[normalize-space()='']//a[@href='#']")
    LOGIN_BUTTON=(By.XPATH, "//button[@type='submit']")
    LOGOUT=(By.XPATH, "//span[normalize-space()='Logout']")
    INVAILID_PASS=(By.XPATH, "//label[normalize-space()='Wrong email or password.']")
    INVAILID_EMAIL=(By.XPATH,"//label[normalize-space()='E-Mail address invalid']")
    INVALID_MOBILE=(By.XPATH,"//label[normalize-space()='Invalid mobile number']")
    PHONE_NO_INPUT=(By.XPATH,"//input[@id='r-phone']")
    BLANK_EMAIL=(By.XPATH,"//label[normalize-space()='E-Mail address is required']")
    BLANK_PASS=(By.XPATH,"//label[normalize-space()='Password is required']")
    LOGIN_LINK=(By.XPATH,"//a[contains(text(),'Login')]")
    WRONG_PASSWORD_MESSAGE=(By.XPATH,"//label[@class='error-label text-left']")
    
    def click_on_login_link(self):
        self.context.browser.find_element(*self.LOGIN_LINK).click()
        time.sleep(5)
        
    def click_on_login(self):
        self.context.browser.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(15)
        
    def click_on_user_icon(self):
        self.helper.explicit_wait(self.USER_ICON).click()
        time.sleep(5)
    def logout(self):
        self.helper.explicit_wait(self.LOGOUT).click()
        
    def invalid_msg_for_mail(self):    
        excpected_msg=self.context.browser.find_element(*self.INVAILID_EMAIL).text
        actual_msg="E-Mail address invalid"
        test.assertEqual(excpected_msg,actual_msg)
     
    def invalid_msg_for_pass(self):
        excpected_msg=self.context.browser.find_element(*self.INVAILID_PASS).text
        actual_msg="Wrong email or password."
        test.assertEqual(excpected_msg,actual_msg)
        
    def invalid_msg_for_mobile(self):   
        excpected_msg=self.context.browser.find_element(*self.INVALID_MOBILE).text
        actual_msg="Invalid mobile number"
        test.assertEqual(excpected_msg,actual_msg)
        
    def blank_email(self):
        excpected_msg=self.context.browser.find_element(*self.BLANK_EMAIL).text
        actual_msg="E-Mail address is required"
        test.assertEqual(excpected_msg,actual_msg)
    
    def blank_pass(self):
        self.context.browser.find_element(*self.BLANK_PASS).click()
        excpected_msg=self.context.browser.find_element(*self.BLANK_PASS).text
        actual_msg="Password is required"
        test.assertEqual(excpected_msg,actual_msg)
        
    def create_wrong_password(self):
        excpected_msg=self.helper.explicit_wait(self.WRONG_PASSWORD_MESSAGE).text
        actual_msg="Minimum password length should be 6 symbols"
        test.assertEqual(excpected_msg,actual_msg)
        
    def phone(self,phone_number):
        self.context.browser.find_element(*self.PHONE_NO_INPUT).send_keys(phone_number)
        
    