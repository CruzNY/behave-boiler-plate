from features.steps.common_steps import CommonSteps as common
from behave import *

class SimpleSteps():
    def click_on_element(context,element):
        element = context.browser.find_element(element)
        common.click(element)