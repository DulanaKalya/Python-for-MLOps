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
    filename='applog.log',  # Log file name
    filemode='w'            # Overwrite each time; use 'a' to append
)
