import time

from pages.basepage import BasePage
from pages.homepage import HomePage
# from pages.login_page import Login
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import Login


def before_all(context):
    context.browser = webdriver.Chrome(r"C:\Users\deept\OneDrive\Desktop\Project\Finexity_testing_using_behave\finexity_project\driver\chromedriver.exe")
    # context.browser = webdriver.Firefox(r"C:\Users\deept\OneDrive\Desktop\New folder\driver\geckodriver.exe")
def before_feature(context,feature):
    # context.browser = webdriver.Chrome(r"C:\Users\deept\OneDrive\Desktop\New folder\driver\chromedriver.exe")
    context.browser.get("https://test.finexity.com/")
    time.sleep(5)
    context.browser.maximize_window()
    context.browser.find_element(By.XPATH,
                                '//*[@id="cookiefirst-root"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/button').click()  
    time.sleep(5)
def before_scenario(context,scenario):
    context.browser = webdriver.Chrome(r"C:\Users\deept\OneDrive\Desktop\New folder\driver\chromedriver.exe")
    context.browser.get("https://test.finexity.com/")
    time.sleep(5)
    context.browser.maximize_window()
    context.browser.find_element(By.XPATH,
                                '//*[@id="cookiefirst-root"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/button').click()  
    
    context.basepage=BasePage(context)
    context.publicpage=(context)
    context.homepage=HomePage(context)
    context.login=Login(context)
    
def after_scenario(context,scenario):
	context.browser.quit() 
