# logger.py
import logging

# Clear existing handlers (important for Jupyter and imports)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Set up logging to file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ArithmethicApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b},={result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Adding {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,15)
divide(10,0)