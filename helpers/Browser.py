from distutils.command.config import config
import os

from helpers.WebHelper import get_browser


my_file = (os.path.join(os.getcwd(),'setup.cfg'))
config(my_file)

#reading the browser type from the configuration file 
helper_func = get_browser(config.get('Environment', "Browser"))
