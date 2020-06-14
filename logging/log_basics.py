
'''logging is a powerful, built-in module

By default, only high severity levels of WARNING and above are shown
'''
import logging
import time

# Default severity level from low to high
# Default level set in basicConfig() is logging.WARNING
# - which means at and above this severity level will now get logged

# Once following logging function is called first, following basicConfig() 
# will not be effective.

#logging.error('Test error message') 

logging.basicConfig(level=logging.WARNING, filename="log.txt", 
        filemode='a',
        datefmt='%Y-%b-%d %H-%M-%S',
        format='%(asctime)s %(name)s-%(levelname)s-%(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


