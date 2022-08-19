# this module contains the element locators for the login pages
# TODO create variables with the proper selector and it's webelement location in DOM (xpath,css,id,class... etc)
from selenium.webdriver.common.by import By

xpath = By.XPATH

email = xpath, "//span/following-sibling::input[@name='email']"
password = By.XPATH, "//span/following-sibling::input[@name='password']"
login_button = By.XPATH, "//button/span[text()='Login']"
login_page_verification = By.XPATH, "//h5[text()='Login']"
reset_password = By.XPATH, "//label[text()='Reset Password']"
signup_button = By.XPATH, "//span[contains(text(),'Signup')]"

