from features.steps.common_steps import CommonSteps
from behave import when, then
class SimpleSteps(CommonSteps):
    def __init__(self):
        super().__init__()

    def click_on_web_element(self,context, element_str):
        element = context.browser.find_by_name(element_str)
        self.click(element)

    @then ('I click on the {arg} element||button||icon')
    def click_on_element(self,context,element_str):
        element = context.browser.find_by_name(element_str)
        self.click(element)

    @when('I enter {arg1} in the {arg2} field||textbox||textarea')
    def enter_text(self,context, text, web_element):
        element = context.browser.find_by_id(web_element)
        self.clear_and_enter_text(text,element);

    @then('I verifty that the {element} is "{displayed}"')
    def element_is_displayed(self,element,displayed,context):
        print(displayed)
        if displayed.contains('not'):
            element = context.find_element(element[0],element[1])
            assert(not self.is_displayed(element))
        element = context.find_element(element[0],element[1])
        assert(self.is_displayed(element))