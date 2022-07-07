from selenium import webdriver

from helpers.HelperFunc import HelperFunc

def get_browser(browser):
    if browser == 'chrome':
        return HelperFunc(webdriver.Chrome())