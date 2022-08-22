class CommonSteps():
    def click(self, web_element):
        web_element.click()
    
    def clear_and_enter_text(self,text,web_element):
        """
        CLears field and enters text
        """
        web_element.clear()
        web_element.send_keys(text)

    def select_from_dropdown(value,web_dropdown):
        pass

    def is_displayed(web_element):
        '''
        returns true when element is displayed. 
        '''
        pass

    def is_enabled(web_element):
        '''
        returns true when element is enabled
        '''
        pass

