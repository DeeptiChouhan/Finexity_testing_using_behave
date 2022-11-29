import time
from behave import *

from pages.basepage import BasePage
from pages.registartion import Registration

@when(u'User clicks on registration link')
def step_impl(context):
    context.registration.clickOnRegistrationLink()
    
@when(u'User is on registration page')
def step_impl(context):
    context.registration.match_registration_page_content()

@when(u'User provides registration email as "testuser14@finexity.com"')
def step_impl(context):
    context.registration.enter_email()
    
@when(u'User clicks on Create Account button')
def step_impl(context):
    context.registration.click_on_create_account()

@when(u'User clicks on Generic Continue button')
def step_impl(context):
   context.registration.click_on_continue()
   
@when(u'User provides registration password as "tests!rock"')
def step_impl(context):
    context.registration.create_password()

@then(u'Verify that new user registration was successful')
def step_impl(context):
    context.registration.registerSuccessful()

@when(u'User clicks on Exit Registration button')
def step_impl(context):
    context.homepage.exitButton()

@when(u'User clicks on Login link')
def step_impl(context):
    context.login.click_on_login_link()

@then(u'User enters credentials "<username>" and "<password>" for Finexity')
def step_impl(context,username,password):
    context.browser.find_element(*BasePage.USERNAME_INPUT).send_keys(username)
    context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
    
@when(u'User provides registration mobile_number as "999999"')
def step_impl(context):
    context.registration.enter_mobile()

@when(u'User clicks on Generic Continue button with 1 error handled')
def step_impl(context):
    context.login.blank_pass()

@when(u'User provides registration password as "{password}"')
def step_impl(context,password):
    context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
    time.sleep(5)

@then(u'Verify error message "Minimum password length should be 6 symbols"')
def step_impl(context):
    context.login.create_wrong_password()
    