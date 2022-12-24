import os,sys
sys.path.append(os.getcwd())
from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifacts_entity
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.components import data_ingestion,data_validation
if __name__=="__main__":
    try:
        #data_ingestion
        training_pipeline_config=config_entity.TrainingPipelineConfig()
        data_ingestion_config=config_entity.DataIngestionConfig(training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion_=data_ingestion.DataIngestion(data_ingestion_config)
        data_ingestion_artifact=data_ingestion_.initiate_data_ingestion()
        print("DATA INGESTION ARTIFACT")
        print(data_ingestion_artifact)
        #data_validation
        data_validation_config=config_entity.DataValidationConfig(training_pipeline_config)
        data_validation_=data_validation.DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact=data_validation_.initiate_data_validation()
        print("DATA VALIDATION ARTIFACT")
        print(data_validation_artifact)
    except Exception as e:
        raise SensorException(e,sys)