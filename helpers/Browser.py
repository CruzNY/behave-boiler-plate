from distutils.command.config import config
import os

from helpers.driver_generator import get_browser


my_file = (os.path.join(os.getcwd(),'setup.cfg'))
config(my_file)

#reading the browser type from the configuration file 
browser = get_browser(config.get('Environment', "Browser"))
