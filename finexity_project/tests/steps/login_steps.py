import time
from pages.basepage import BasePage
from behave import given,when,then,step

@when('user enters "{username}" and "{password}"')
def step_implpy(context, username, password):
      context.browser.find_element(*BasePage.USERNAME_INPUT).send_keys(username)
      context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
      
@when(u'User clicks on Login button')
def step_impl(context):
      context.login.click_on_login()
    
@then(u'user should be logged in')
def step_impl(context):
    pass
 
@then(u'Verify that dashboard is displayed')
def step_impl(context):
    context.homepage.click_on_dashbord_botton()

@when(u'User clicks the option to log out by clicking the user icon')
def step_impl(context):
      context.login.click_on_user_icon()
                  
@when(u'user click on logout option')
def step_impl(context):
      context.login.logout()
      time.sleep(5)
      
@given(u'refresh browser')
def step_impl(context):
    context.browser.refresh()
    time.sleep(2)
    
@when(u'E-Mail address invalid message should be show')
def step_impl(context):
    context.login.invalid_msg_for_mail()
     
@when(u'Wrong email or password. should be show')
def step_impl(context):
    context.login.invalid_msg_for_pass()
    
@when(u'E-Mail address is required should be show')
def step_impl(context):
    context.login.blank_email()  
     
@when(u'Password is required should be show')
def step_impl(context):
    context.login.blank_pass()
    
@when(u'user enters "" and "tests!rock"')
def step_impl(context):
    pass

@when(u'user enters "testuser01@finexity.com" and ""')
def step_impl(context):
    pass


    