import logging
import os
from datetime import datetime
import sys
sys.path.append(os.getcwd())

LOG_FILE_NAME=f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
LOG_FILE_DIR=os.path.join("logs")
os.makedirs(LOG_FILE_DIR,exist_ok=True)
LOG_FILE_PATH=os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)
logging.basicConfig(filename=LOG_FILE_PATH,format="%(asctime)s %(message)s",level=logging.INFO)