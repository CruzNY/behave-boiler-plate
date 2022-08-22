#from selenium import webdriver
#import os
#from configparser import ConfigParser
#from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then
from steps.simple_steps import SimpleSteps
simple_steps = SimpleSteps()
@given(u'I go to 4davanceboy to add item')
def step(context):
    print('steps')
    context.browser.open('https://lambdatest.github.io/sample-todo-app/')
    context.browser.maximize()
 
@then(u'I Click on first checkbox and second checkbox')
def click_on_checkbox_one(context):
    # context.browser.find_by_name('li1').click()
    simple_steps.click_on_element(context,'li1')
    context.browser.find_by_name('li2').click()
 
@when(u'I enter item to add')
def enter_item_name(context):
    context.browser.find_by_id('sampletodotext').send_keys("Yey, Let's add it to list")
    
 
@when(u'I click add button')
def click_on_add_button(context):
    context.browser.find_by_id('addbutton').click()
 
@then(u'I should verify the added item')
def see_login_message(context):
    added_item = context.browser.find_by_xpath("//span[@class='done-false']").text
 
    time.sleep(10)
 
    if added_item in "Yey, Let's add it to list":
        return True
    else:
        return False