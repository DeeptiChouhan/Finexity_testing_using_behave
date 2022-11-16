from behave import then, given

@given(u'User on Finexity')
def step_impl(context):
    print("HElo")
    context.homepage.click_on_logo()
    print("HElo")
    
@then(u'Then Header text as Invest in alternative assets. Fully digital and flexible. is displayed on home page')
def step_impl(context):
    context.homepage.check_header_text_on_home_page()

@then(u'Verify top manu content')
def step_impl(context):
    context.homepage.top_manu()

@then(u'Verify menu bar content under Personal in English')
def step_impl(context):
    context.homepage.check_EN()
   
@then(u'Join now botton available in home page')
def step_impl(context):
    context.homepage.join_now()
   