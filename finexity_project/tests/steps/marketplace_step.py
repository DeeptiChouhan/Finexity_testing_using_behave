import json
from behave import *
from tests.pages.basepage import BasePage
    
@when(u'user select \'Green Tiny House Jan Vacation Property\' property from Investments tab')
def step_impl(context):
    context.marketplace.select_product_for_invesment()
@when(u'user click on Invest now button')
def step_impl(context):
    context.marketplace.clickOnInvestNow()
    
@when(u'user enter amount')
def step_impl(context):
    context.marketplace.enterYourInvestment()
  
@then(u'clicks on continue button')
def step_impl(context):
    context.basepage.click_on_continue()

@then(u'user clicks on start button')
def step_impl(context):
    context.marketplace.clickOnStart()

@when(u'user select payment method')
def step_impl(context):
    context.basepage.click_on_continue()

@then(u'user clicks on Costs and grants')
def step_impl(context):
    context.basepage.click_on_continue()

@then(u'user allow all the terms and condition')
def step_impl(context):
    context.marketplace.acceptAlltermsAndCondition()
    
@then(u'clicks on buy now on Overview page')
def step_impl(context):
    context.marketplace.clickOnBuyNow()
    
@then(u'user click on back to roduction page')
def step_impl(context):
    context.marketplace.back_to_product_page()