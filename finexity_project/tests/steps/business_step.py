from behave import *
from selenium.webdriver.common.by import By
from pages.business_page import Business
BUSINESS_TAB=(By.XPATH,"//div[@class='desktop-display']//li[@class='li-menu-item']")
@when(u'user clicks on business tab of hpme page')
def step_impl(context):
    context.browser.find_element(*Business.BUSINESS_TAB)
   
    context.business.click_on_business()

@when(u'user hoverover on solution option')
def step_impl(context):
    context.business.check_all_option_of_solution()

@when(u'solution pop should be open')
def step_impl(context):
    pass

@when(u'user clicks on any option')
def step_impl(context):
    context.business.check_all_option_of_solution()

@when(u'page should be option')
def step_impl(context):
    pass

@when(u'user hoverover on discover option')
def step_impl(context):
    context.business.hoverover_in_discover()

@when(u'discover pop should be open')
def step_impl(context):
    context.business.check_all_option_of_discover()

@when(u'user hoverover on company option')
def step_impl(context):
   context.business.hoverover_in_discover()

@when(u'company pop should be open')
def step_impl(context):
    context.business.check_all_option_of_company()
    
@when(u'Verify top manu content')
def step_impl(context):
    pass


@when(u'Verify that header is displayed')
def step_impl(context):
    pass