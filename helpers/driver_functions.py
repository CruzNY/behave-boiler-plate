from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class DriverFunctions(object):
    __TIMEOUT = 10
 
    def __init__(self, driver):
        super(DriverFunctions, self).__init__()
        self._driver_wait = WebDriverWait(driver, DriverFunctions.__TIMEOUT)
        self._driver = driver
 
    def open(self, url):
        """
        Go to url
        """
        self._driver.get(url)
 
    def maximize(self):
        self._driver.maximize_window()        

    def close(self):
        """
        closes the browser
        """
        self._driver.quit()
    # Helper functions that are used to identify the web locators in Selenium Python tutorial  
 
    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
 
    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
 
    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id))) 

    def find_element(self,element):
        return self._driver.find_element(element[0],element[1])