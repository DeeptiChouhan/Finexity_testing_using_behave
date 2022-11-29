
import time

from pages.basepage import BasePage
from pages.homepage import HomePage
from pages.login_page import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.business_page import Business
from pages.login_page import Login
from pages.exclusive_page import ExclusivePage
from pages.marrketplace import Marketplace
from pages.registartion import Registration



def before_all(context):
    context.browser = webdriver.Chrome(r"driver\chromedriver.exe")

def before_feature(context,feature):
    context.browser.get("https://test.finexity.com/")
    time.sleep(5)
    context.browser.maximize_window()
    context.browser.find_element(By.XPATH,
                                '//*[@id="cookiefirst-root"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/button').click()  
    time.sleep(7)
    
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
