class CommonSteps():

    def click(element):
        element.click()
    
    def clear_and_enter_text(text,element):
        element.clear()
        element.send_keys(text)

    def select_from_dropdown():
        pass

    def is_displayed(element):
        return element.is_displayed()

    def is_enabled():
        pass

