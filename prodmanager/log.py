import sys
import logging

def init_logger(level="DEBUG"):
  logger = logging.getLogger('ProdManager')
  handler = logging.StreamHandler(sys.stdout)
  handler.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'))
  logger.addHandler(handler)
  logger.setLevel(level)

  return logger
