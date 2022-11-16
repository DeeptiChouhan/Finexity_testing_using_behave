from behave import when ,then,given


@when(u'user should be on login page')
def step_impl(context):
    context.login.login_page()

@when(u'user clicks on logo')
def step_impl(context):
    context.homepage.click_on_logo()

@then(u'Verify that footer is displayed')
def step_impl(context):
    context.homepage.footer()
    
@when(u'User clicks on Dashboard button')
def step_impl(context):
    context.homepage.click_on_dashbord_botton()