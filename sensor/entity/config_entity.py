import os,sys
sys.path.append(os.getcwd())
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

FILE_NAME="sensor.csv"
TRAIN_FILE_PATH="train.csv"
TEST_FILE_PATH="test.csv"

class TrainingPipelineConfig:
    '''
    Description: This class is used to store the configuration for training pipeline
    ============================================
    Input: None
    Output: None
    =============================================
    '''
    def __init__(self):
        try:
            self.artifact_dir=os.path.join("artifacts",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise SensorException(e,sys)

class DataIngestionConfig:
    '''
    Description: This class is used to store the configuration for data ingestion
    ============================================
    Input: training_pipeline_config:TrainingPipelineConfig
    Output: None
    =============================================
    return None
    '''
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="sensor-database"
            self.collection_name="sensor-data"
            self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data-ingestion")
            self.feature_store_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_PATH)
            self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_PATH)
            self.test_size=0.25
        except Exception as e:
            raise SensorException(e,sys)

    def to_dict(self):
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)