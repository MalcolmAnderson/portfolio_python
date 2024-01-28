import logging 

def logger_factory():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : %(message)s')
    file_handler = logging.FileHandler('portfolio_python.log')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

# access using the following
#   import mba_logging as log
#   logger = log.logger_factory()
#   # log.logging.getLogger().setLevel(log.logging.DEBUG)


# to change logging level in you file use the following
#   log.logging.getLogger().setLevel(log.logging.DEBUG)

# In theory, this technique can be used at run time to change logging levels on demand
# i.e. 
#   change logging level to debug
#   run problematic transaction
#   change logging level back to info
# see https://stackoverflow.com/questions/19617355/dynamically-changing-log-level-without-restarting-the-application
