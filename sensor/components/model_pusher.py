from sensor.exception import SensorException
from sensor.logger import logging
from sensor.predictor import ModelResolver
import sys
from sensor.utils import load_object,save_object
from sensor.entity.artifacts_entity import DataTransformationArtifact
from sensor.entity.artifacts_entity import ModelTrainerArtifact
from sensor.entity.artifacts_entity import ModelPusherArtifact
from sensor.entity.config_entity import ModelPusherConfig

class ModelPusher(object):
    def __init__(self,model_pusher_config:ModelPusherConfig,
    data_transformation_artifact:DataTransformationArtifact,
    model_trainer_artifact:ModelTrainerArtifact):
        try:
            logging.info(f"{'>>>'*20} Model Pusher {'<<<'*20}")
            self.model_pusher_config=model_pusher_config
            self.data_transformation_artifact=data_transformation_artifact
            self.model_trainer_artifact=model_trainer_artifact
            self.model_resolver=ModelResolver(model_registry=self.model_pusher_config.save_model_dir)
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_pusher(self):
        try:
            logging.info("Model Pusher is initiated")
            transformer=load_object(file_path=self.data_transformation_artifact.transformed_object_path)
            model=load_object(file_path=self.model_trainer_artifact.model_path) 
            target_encoder=load_object(file_path=self.data_transformation_artifact.target_encoder_path)

            #model pusher dir
            logging.info("Saving Model into model pusher dir")
            save_object(obj=transformer,model=self.model_pusher_config.pusher_transformer_path)
            save_object(obj=model,model=self.model_pusher_config.pusher_model_path)
            save_object(obj=target_encoder,model=self.model_pusher_config.pusher_target_encoder_path)

            #saved model dir
            logging.info("Saving Model into saved model dir")
            transformed_path=self.model_resolver.get_latest_save_transformer_path()
            model_path=self.model_resolver.get_latest_save_model_path()
            target_encoder_path=self.model_resolver.get_latest_save_target_encoder_path()

            save_object(obj=transformer,model=transformed_path)
            save_object(obj=model,model=model_path)
            save_object(obj=target_encoder,model=target_encoder_path)

            model_pusher_artifact=ModelPusherArtifact(pusher_model_dir=self.model_pusher_config.pusher_model_dir,saved_model_dir=
            self.model_pusher_config.save_model_dir)
            logging.info(f"Model Pusher is completed {model_pusher_artifact}")
            return model_pusher_artifact
        except Exception as e:
            raise SensorException(e,sys)