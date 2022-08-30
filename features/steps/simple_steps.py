from features.steps.common_steps import CommonSteps as common
from behave import *

class SimpleSteps():
    """
    following methods are to be called from a respective Page Steps
    """
    def click_on_element(context,element):
        """
        click_on_element clicks on provided element
        :param element: is element passed from the Page Object
        """
        web_element = context.browser.find_element(element)
        common.click(web_element)

    def enter_text(context,text,field):
        web_element = context.browser.find_element(field)
        common.clear_and_enter_text(text,web_element)

    def is_displayed(context,element):
        web_element = context.browser.find_element(element)
        common.is_displayed(web_element)
