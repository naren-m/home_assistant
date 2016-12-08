import logging

# logging.basicConfig(level=logging.INFO)
FORMAT = '%(asctime)s - %(name)s - %(levelname)s  - %(filename)s:%(lineno)s - %(funcName)s() : %(message)s'

logging.basicConfig(filename='example.log',
	format= FORMAT,
	level=logging.DEBUG,
	datefmt='%m/%d/%Y %I:%M:%S')

logger = logging.getLogger(__name__)
