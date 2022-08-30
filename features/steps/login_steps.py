# contains steps to be used on the login page.
from features.pages import login
from features.steps.simple_steps import SimpleSteps as simple
from behave import *

@given('go to url')
def step(context):
    context.browser.open("https://phptravels.net/login")

@then('click on login')
def step2(context):
    simple.click_on_element(context,login.email)

@then('enter text')
def dep(context):
    simple.enter_text(context,"alexcruz182@gmail.com",login.email)

@then('check if displayed')
def asf(context):
    simple.is_displayed(context,login.email)