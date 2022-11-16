import time
from behave import given,when,then
from selenium.webdriver.common.by import By

# @when(u'enter username "{username}" and password "{password}"')
# def step_impl(context,username,password):
#         # context.login.enter_user_cred()
#         context.browser.find_element(By.XPATH, "//input[@id='l-email']").send_keys(username)
#         time.sleep(5)
#         context.browser.find_element(By.XPATH, "//input[@id='l-password']").send_keys(password)
#         time.sleep(5)

# @when(u'click on login')
# def step_impl(context):
#     context.login.click_on_login()
    
    

@given('user enters "{username}" and "{password}"')
def step_implpy(context, username, password):
      print("Username for login: {}".format(username))
      print("Password for login: {}".format(password))
      context.browser.find_element(By.XPATH, "//input[@id='l-email']").send_keys(username)
      time.sleep(5)
      context.browser.find_element(By.XPATH, "//input[@id='l-password']").send_keys(password)
      time.sleep(5)
@then('user should be logged in')
def step_implpy(context):
      try:
            context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
      except:
            context.logger.error()
      