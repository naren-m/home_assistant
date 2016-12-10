import logging

# logging.basicConfig(level=logging.INFO)
FORMAT = '%(asctime)s - %(name)s - %(levelname)s  - %(filename)s:%(lineno)s - %(funcName)s() : %(message)s'

logging.basicConfig(filename='example.log',
	format= FORMAT,
	level=logging.DEBUG,
	datefmt='%m/%d/%Y %I:%M:%S')
# file handler to keep size of log file in check
# import logging
# import logging.handlers
# handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024*512, backupCount=1)
# handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024*512, backupCount=1)
# formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(threadName)s : %(message)s')
# handler.setFormatter(formatter)

# app_logger.addHandler(handler)
# app_logger.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
