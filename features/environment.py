from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag
from helpers.driver_generator import DriverGenerator

 
def before_all(context):
    browser_inst = DriverGenerator.generate_driver()
    # TODO change this to browser
    context.browser = browser_inst    
    # Local Chrome WebDriver
    #if context.browser == "chrome":
    #   context.driver = webdriver.Chrome()
 
def after_all(context):
    context.browser.close()