import time
from pages.basepage import BasePage
from pages.homepage import HomePage
from pages.login_page import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.business_page import Business
from pages.login_page import Login
from pages.exclusive_page import ExclusivePage
from pages.marketplace import Marketplace
from pages.registration import Registration
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
        
def before_feature(context,feature):  
    login=Login(context) 
    context.browser = webdriver.Chrome(executable_path=r"driver\chromedriver.exe")
    TOKEN = open("./tests/configs/token.txt", "r")
    TOKEN_ACCESS = TOKEN.read()
    context.browser.get("https://test.finexity.com/"+TOKEN_ACCESS)
    context.browser.maximize_window()
    time.sleep(5)
    login.click_on_login_link()
   
    
def before_scenario(context,scenario):
    context.basepage=BasePage(context)
    context.publicpage=(context)
    context.homepage=HomePage(context)
    context.login=Login(context)
    context.exclusive=ExclusivePage(context)
    context.business=Business(context)
    context.marketplace=Marketplace(context)
    context.registration=Registration(context)
    
def after_feature(context,feature):
    context.browser.quit() 
