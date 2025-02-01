# Loggger
'''
import logging

logging.debug("Debug Error occured in code.")
logging.info("Info: Admin logged in.")
logging.warning("Warning: Less hard disk space")
logging.error("Error: File not found exception")
logging.critical("Critical: App crashed")
# In this way we need to write the logs in the production

####  In the result you won't find the debug and info logger, to get the logs of debug and info logger then use below format


# ---------------------
# Loggger

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug Error occured in code.")
logging.info("Info: Admin logged in.")
logging.warning("Warning: Less hard disk space")
logging.error("Error: File not found exception")
logging.critical("Critical: App crashed")
# In this way we need to write the logs in the production

# ---------------------
# Loggger

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="mylog.log",filemode='w') # To store tehe logs in a fuile

logging.debug("Debug Error occured in code.")
logging.info("Info: Admin logged in.")
logging.warning("Warning: Less hard disk space")
logging.error("Error: File not found exception")
logging.critical("Critical: App crashed")
# In this way we need to write the logs in the production


# ---------------------
# Loggger

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="mylog.log",filemode='w',
            format="Python-app : %(name)s-%(levelname)s-%(message)s-%(asctime)s-%(process)d") # Special PEG parse programming passsing the values, %s is used to pass string, %d for int

logging.debug("Debug Error occured in code.")
logging.info("Info: Admin logged in.")
logging.warning("Warning: Less hard disk space")
logging.error("Error: File not found exception")
logging.critical("Critical: App crashed")
# In this way we need to write the logs in the production

username="Mahendra"
logging.info(f"{username} has logged in")

'''

# ---------------------
# Loggger

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="mylog.log",filemode='w',
            format="Python-app : %(name)s-%(levelname)s-%(message)s-%(asctime)s-%(process)d") # Special PEG parse programming passsing the values, %s is used to pass string, %d for int

logging.debug("Debug Error occured in code.")
logging.info("Info: Admin logged in.")
logging.warning("Warning: Less hard disk space")
logging.error("Error: File not found exception")
logging.critical("Critical: App crashed")
# In this way we need to write the logs in the production

username="Mahendra"
logging.info(f"{username} has logged in")



try:
    a=10
    b=0
    c=a/b
    
except Exception as ex:  # We are trying to log the real time execptions using the try except approach and printing it in the log file using exc_info=True
    logging.error("Exception occured",exc_info=True)