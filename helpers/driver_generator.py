from configparser import ConfigParser
from distutils.command.config import config
import os

from helpers.browser import get_browser
class DriverGenerator():

    def generate_driver():
        config = ConfigParser()
        my_file = (os.path.join(os.getcwd(),'setup.cfg'))
        config.read(my_file)
        browser = get_browser(config.get('Environment', "Browser"))
        return browser

