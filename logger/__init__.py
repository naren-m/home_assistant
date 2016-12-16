import logging
import logging.handlers

LOG_FILENAME = '../example.log'
FORMAT = '%(asctime)s-%(levelname).4s-%(funcName)s()-%(filename)s:%(lineno).3d : %(message)s'

app_logger = logging.getLogger(__name__)
# file handler to keep size of log file in check
# handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024*512, backupCount=1)
# handler.setFormatter(FORMAT)
# app_logger.addHandler(handler)

"""
Level   Numeric value
CRITICAL    50
ERROR   40
WARNING 30
INFO    20
DEBUG   10
NOTSET  0
"""

logging.basicConfig(filename=LOG_FILENAME,
	format= FORMAT,
	level=logging.DEBUG,
	datefmt='%m/%d/%Y %I:%M:%S')

info = app_logger.info
debug = app_logger.debug
warning = app_logger.warning
error =  app_logger.error
critical = app_logger.critical
log = app_logger.log
exception = app_logger.exception

