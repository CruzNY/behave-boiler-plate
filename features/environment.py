from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag

from helpers.driver_generator import get_browser

 
def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
 
    # Reading the browser type from the configuration file for Selenium Python Tutorial
    browser_inst = get_browser(config.get('Environment', 'Browser'))
    # TODO change this to browser
    context.browser = browser_inst
    
    # Local Chrome WebDriver
    #if context.browser == "chrome":
    #   context.driver = webdriver.Chrome()
 
def after_all(context):
    context.browser.close()