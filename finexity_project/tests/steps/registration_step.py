import time
from behave import *
from pages.basepage import BasePage
from pages.registartion import Registration
from pages.login_page import Login

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

@when(u'User clicks on Continue button')
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

@when(u'User clicks on Continue button with 1 error handled')
def step_impl(context):
    context.browser.find_element(*Registration.EMAIL_INPUT).click()
    
@when(u'User provides registration password as {password}')
def step_impl(context,password):
    context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
    time.sleep(5)

@then(u'Verify error message "Minimum password length should be 6 symbols"')
def step_impl(context):
    context.login.create_wrong_password()

@then(u'Verify error message "Password is required"')
def step_impl(context):
    context.login.blank_pass()
    
@when(u'User tries to register without entering the password then')
def step_impl(context):
    context.browser.find_element(*Registration.PASSWORD_INPUT).click()
    context.browser.find_element(*Registration.EMAIL_INPUT).click()
    
@then(u'User provides registration email as "{username}"')
def step_impl(context,username):
    context.browser.find_element(*Registration.EMAIL_INPUT).send_keys(username)

@then(u'Verify error message E-Mail address invalid')
def step_impl(context):
    context.login.invalid_msg_for_mail()
    
@then(u'User provides registration mobile_number as "{mobile_number}"')
def step_impl(context,mobile_number):
   context.browser.find_element(*Registration.EMAIL_INPUT).send_keys(mobile_number)

@then(u'Verify error message Invalid mobile number')
def step_impl(context):
    context.login.invalid_msg_for_mobile()

@then(u'Verify that user is redirected to User-onboarding page')
def step_impl(context):
    time.sleep(5)
    context.registration.welcome_screen()

@when(u'User clicks on Continue button on Welcome page')
def step_impl(context):
   context.registration.click_on_continue()
   
@when(u'User clicks on Skip button on complete your personal data page')
def step_impl(context):
    context.registration.skip()

@when(u'User clicks on Skip button on Your Interests')
def step_impl(context):
    context.registration.skip()
     
# @when(u'User enters mobile number as "<phone_number>"')
# def step_impl(context,phone_number):
#     context.browser.find_element(*Login.PHONE_NO_INPUT).send_keys(phone_number)
    
@when(u'User enters mobile number as 45645678')
def step_impl(context):
    try:
        context.browser.find_element(*Login.PHONE_NO_INPUT).send_keys("45645678")
        time.sleep(2)
    except:
        pass
    
@when(u'User clicks on Request code button with wait of 5 sec')
def step_impl(context):
    context.registration.request_code()
    time.sleep(5)
   
@when(u'User enters TAN as 999999')
def step_impl(context):
    context.registration.otp_code()
    
@when(u'User waits for 10 sec')
def step_impl(context):
    time.sleep(10)
    
@when(u'User checks all tick boxes')
def step_impl(context):
    context.registration.tick_on_check_boxes()

@when(u'User clicks on Continue button on Conditions page')
def step_impl(context):
   context.registration.click_on_continue()

@when(u'User clicks on To Dashboard button on Congratulations page')
def step_impl(context):
    context.registration.click_on_continue()

@when(u'Verify that user is redirected to Dashboard page')
def step_impl(context):
    context.homepage.dashboard_text()
