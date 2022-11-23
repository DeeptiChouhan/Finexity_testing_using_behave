
from behave import *
@given(u'User is on Finexity website')
def step_impl(context):
    pass
@when(u'user clicks on logo')
def step_impl(context):
    context.homepage.click_on_logo()

@then(u'Verify top menu content')
def step_impl(context):
    context.homepage.top_menu()

@then(u'Verify that header is displayed')
def step_impl(context):
    context.basepage.header()

@when(u'Verify that footer is displayed')
def step_impl(context):
    context.basepage.footer()
    
@when(u'user click on personal tab')
def step_impl(context):
    context.homepage.click_on_personal()

@when(u'user click on join now botton on personal tab')
def step_impl(context):
    context.homepage.click_on_join_now_tab()
    
@when(u'user clicks on register now botton on personal tab')
def step_impl(context):
    context.homepage.click_on_register_now()
    
@when(u'user check that footer links')
def step_impl(context):
    context.homepage.ckeck_footer_links()