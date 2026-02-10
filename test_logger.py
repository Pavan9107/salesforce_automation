import logging

logging.basicConfig(filename="logs.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Test started")
logging.debug("Test debug message")
logging.warning("Test warning message")
logging.error("Test error message")