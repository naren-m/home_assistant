import logger

#logger = app_logger.logger


def naren():
	logger.info('Start reading database')
	records = {'john': 55, 'tom': 66}
	logger.debug('Records: %s', records)
	logger.info('Updating records ...')
	logger.warning('warning records ...')
	logger.info('Finish updating records')

naren()
