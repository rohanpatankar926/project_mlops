from sensor.logger import logging
import sys
from sensor.exception import SensorException

def dummy(a:int,v:float):
    try:
        if a==1:
            raise SensorException("Error",sys)
    except SensorException as e:
        logging.error(e)
        return False
    return True
if __name__=="__main__":
    print(dummy(1,1.0))