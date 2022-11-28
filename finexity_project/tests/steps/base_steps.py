from behave import when ,then,given


@then(u'Verify that footer is displayed')
def step_impl(context):
    context.basepage.footer()
    
@when(u'User clicks on Dashboard button')
def step_impl(context):
    context.basepge.footer()