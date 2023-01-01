from sensor.pipeline import training
from sensor.exception import SensorException
from sensor.pipeline import batch_prediction
import sys

print(__name__)

input_func_name=input("Please enter the function name for training or batch pred: ")

if __name__ == "__main__":
    def main():
        try:
            if input_func_name=="training":
                run_train=training.start_training_pipeline()
                return run_train
            elif input_func_name=="batch_pred":
                run_batch=batch_prediction.start_batch_prediction()
                return run_batch
        except Exception as e:
            raise SensorException(e,sys)