import os
from loguru import logger
from twisted.logger import Logger, globalLogBeginner, textFileLogObserver

# Ensure the logMailSv directory exists
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logMailSv')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure loguru for general server logs
logger.add(os.path.join(log_dir, "log_server.log"), rotation="1 MB", retention="10 days", level="INFO", encoding="utf-8")

# Configure twisted.logger for Twisted-related logs
globalLogBeginner.beginLoggingTo([textFileLogObserver(open(os.path.join(log_dir, "twisted_server.log"), "a", encoding="utf-8"))])
twisted_logger = Logger()

def get_logger():
    return logger

def get_twisted_logger():
    return twisted_logger
