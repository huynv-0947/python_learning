import logging

logging.debug('DEBUG: {}'.format(logging.DEBUG))
logging.info('INFO: {}'.format(logging.INFO))
logging.warning('WARNING: {}'.format(logging.WARNING))
logging.error('ERROR: {}'.format(logging.ERROR))
logging.critical('CRITICAL: {}'.format(logging.CRITICAL))

# only logs warning, error, critial because logging only logs the messages with a severity level of WARNING or above
# DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50
