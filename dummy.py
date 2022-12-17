from sensor.logger import logging


def dummy(a):
    logging.info(f"This is a dummy function {a}")
    return a

if __name__=="__main__":
    print(dummy(1))