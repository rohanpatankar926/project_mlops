import os,sys
sys.path.append(os.getcwd())
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

FILE_NAME="sensor.csv"
TRAIN_FILE_PATH="train.csv"
TEST_FILE_PATH="test.csv"
TRANSFORMER_OBJECT_FILE_NAME="transformer.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME="target_encoder.pkl"
MODEL_FILE_NAME="model.pkl"

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

    
class DataValidationConfig(object):
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
            try:
                self.database_name="sensor"
                self.collection_name="sensor-data"
                self.data_validation_config=os.path.join(training_pipeline_config.artifact_dir,"data-validation")
                self.report_file_path=os.path.join(self.data_validation_config,"report.yaml")
                self.threshold_missing_value=0.7
                self.base_file_path=os.path.join("aps_failure_training_set1.csv")
            except Exception as e:
                raise SensorException(e,sys)

class DataTransformationConfig(object):
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_transformation_dir=os.path.join(training_pipeline_config.artifact_dir,"data-tranformation")
            self.transform_object_path=os.path.join(self.data_transformation_dir,"transformed",TRANSFORMER_OBJECT_FILE_NAME)
            self.tranformed_train_path=os.path.join(self.data_transformation_dir,"transformed",TRAIN_FILE_PATH.replace("csv","npz"))
            self.transformed_test_path=os.path.join(self.data_transformation_dir,"transformed",TEST_FILE_PATH.replace("csv","npz"))
            self.target_encoder_path=os.path.join(self.data_transformation_dir,"target_encoder",TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise SensorException(e,sys)


class ModelTrainerConfig(object):
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.model_trainer_dir=os.path.join(training_pipeline_config.artifact_dir,"model-trainer")
            self.model_path=os.path.join(self.model_trainer_dir,"model",MODEL_FILE_NAME) 
            self.expected_score=0.8
            self.overfitting_threshold=0.1
        except Exception as e:
            raise SensorException(e,sys)

class ModelEvaluationConfig(object):
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.change_threshold=0.1

class ModelPusherConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_pusher_dir=os.path.join(training_pipeline_config.artifact_dir,"model-pusher")
        self.save_model_dir=os.path.join("saved-models")
        self.pusher_model_dir=os.path.join(self.model_pusher_dir,MODEL_FILE_NAME)
        self.pusher_model_path=os.path.join(self.pusher_model_dir,TRANSFORMER_OBJECT_FILE_NAME) 
        self.pusher_transformer_path=os.path.join(self.pusher_model_dir,TARGET_ENCODER_OBJECT_FILE_NAME)
        self.pusher_target_encoder_path=os.path.join(self.pusher_model_dir,TARGET_ENCODER_OBJECT_FILE_NAME)