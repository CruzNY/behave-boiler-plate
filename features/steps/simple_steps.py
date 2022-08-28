from features.steps.common_steps import CommonSteps as common
from behave import *

class SimpleSteps():
    use_step_matcher("parse")

    @then('User clicks on the "{element}" button')
    def click_on(context,element):
        common.click(context,element)
    
    @given('I go to the "{url}" homepage')
    def go_to(context,url):
        context.browser.open(url)
        

    