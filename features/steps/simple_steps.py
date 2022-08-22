from features.steps.common_steps import CommonSteps
class SimpleSteps(CommonSteps):
    def __init__(self):
        super().__init__()

    def click_on_element(self,context, element_str):
        element = context.browser.find_by_name(element_str)
        self.click(element)

    def enter_text(self,context, text, web_element):
        element = context.browser.find_by_id(web_element)
        self.clear_and_enter_text(text,element);
    