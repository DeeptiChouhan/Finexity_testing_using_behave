import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.basepage import BasePage
class Login(BasePage):
    def __init__(self,context):
        self.context=context
    def enter_user_cred(self,username,password):
        self.context.browser.find_element(By.XPATH, "//input[@id='l-email']").send_keys(username)
        time.sleep(5)
        self.context.browser.find_element(By.XPATH, "//input[@id='l-password']").send_keys(password)
        time.sleep(5)
    def click_on_login(self):
        self.context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(25)
        