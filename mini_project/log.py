import logging

logging.basicConfig(filename='./mini_project/test.log', level = logging.DEBUG)

def log(message):
    logging.info(message)