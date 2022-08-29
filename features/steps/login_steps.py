# contains steps to be used on the login page.
from features.pages import login
from features.steps.simple_steps import SimpleSteps as ss
from behave import *

@given('go to url')
def step(context):
    context.browser.open("https://phptravels.net/login")

@then('click on login')
def step2(context):
    print('before click')    
    ss.click_on_element(context,login.email)
    print('after click')

@then('go to google')
def google(context):
    context.browser.open("https://google.com")