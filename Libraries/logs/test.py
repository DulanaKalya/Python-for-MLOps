from logger import logging

def add(a,b):
    logging.debug("The addition operation is taking place")
    return a+b

logging.debug("The addition fuction is called")
add(10,15)

#### run in terminal python test.py