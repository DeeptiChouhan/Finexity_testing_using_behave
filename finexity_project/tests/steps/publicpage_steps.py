from behave import when,given
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'When User visit on finexity website')
def step_impl(context):
    pass

@when(u'user clicks on personal tab')
def step_impl(context):
    context.publicpage.click_on_personal_tab()
    

@when(u'clicks on register now')
def step_impl(context):
    context.publicpage.click_on_join_now()
    

@when(u'clicks one by one on footer "{Links}"')
def step_impl(context,Links):
    for element in WebDriverWait(context.browser, 15).until(EC.visibility_of_all_elements_located("//footer[@id='mainFooter']/div/div/ul/li")):
            print("clicked on" + element.text+" succsessfully")
            element.click()
    
    

