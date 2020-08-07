import logging
import logging.handlers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fileHandler = logging.handlers.RotatingFileHandler("log1", maxBytes=2, backupCount=2)
#fileHandler = logging.FileHandler("log1")
fileHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(name)-36s %(asctime)s %(levelname)-8s: %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


fileHandler1 = logging.StreamHandler()
fileHandler1.setLevel(logging.ERROR)
formatter = logging.Formatter("%(name)-36s %(asctime)s %(levelname)-8s: %(message)s")
fileHandler1.setFormatter(formatter)
logger.addHandler(fileHandler1)

logger.debug("My name is nitesh")

