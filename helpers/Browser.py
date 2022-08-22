from selenium import webdriver

from helpers.driver_functions import DriverFunctions

def get_browser(browser):
    """
    Returns instance of browser. Type of driver is defined in Environment.py
    """
    if browser == 'chrome':
        return DriverFunctions(webdriver.Chrome())