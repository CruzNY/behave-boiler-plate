from selenium import webdriver

from helpers.driver_functions import DriverFunctions

def get_browser(browser):
    if browser == 'chrome':
        return DriverFunctions(webdriver.Chrome())