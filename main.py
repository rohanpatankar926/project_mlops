import os,sys
sys.path.append(os.getcwd())
from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifacts_entity
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.components import data_ingestion
from sensor.components import data_validation
from sensor.components import data_transformation
from sensor.components import training

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

        #data_tranformation
        data_transformation_config=config_entity.DataTransformationConfig(training_pipeline_config)
        data_transformation_=data_transformation.DataTransformation(transormation_config=data_transformation_config,data_ingestion_artifacts=data_ingestion_artifact)
        data_transformation_artifact=data_transformation_.initiate_data_transformation()
        print("DATA TRANSFORMATION ARTIFACT")
        print(data_transformation_artifact)

        #model_training
        model_training_config=config_entity.ModelTrainerConfig(training_pipeline_config)
        model_training=training.ModelTrainer(model_trainer_config=model_training_config,data_trasformation_artifact=data_transformation_artifact)
        model_training_artifact=model_training.initiate_model_trainer()
        print("MODEL TRAINING ARTIFACT")
        print(model_training_artifact)
    except Exception as e:
        raise SensorException(e,sys)