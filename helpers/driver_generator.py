from configparser import ConfigParser
from helpers.browser import get_browser
import os


class DriverGenerator():
    def generate_driver():
        """
        Generates driver based on Environment.py settigns
        """
        config = ConfigParser()
        my_file = (os.path.join(os.getcwd(),'setup.cfg'))
        config.read(my_file)
        browser = get_browser(config.get('Environment', "Browser"))
        return browser
