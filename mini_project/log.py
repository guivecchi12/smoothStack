import logging

logging.basicConfig(filename='test.log', level = logging.DEBUG)

def log(message):
    logging.info(message)