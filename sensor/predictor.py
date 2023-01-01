import os 
import sys
from sensor.entity.config_entity import TRANSFORMER_OBJECT_FILE_NAME,MODEL_FILE_NAME,TARGET_ENCODER_OBJECT_FILE_NAME
from glob import glob
from sensor.exception import SensorException
sys.path.append(os.getcwd())

class ModelResolver(object):
    def __init__(self,model_registry:str="saved_models",
                    tranformed_dir_name:str="transformer",
                    target_encoder:str="target_encoder",
                    model_dir_name:str="model"):
        self.model_registry=model_registry
        os.makedirs(self.model_registry,exist_ok=True)
        self.tranformed_dir_name=tranformed_dir_name
        self.model_dir_name=model_dir_name
        self.target_encoder_dir=target_encoder

    def get_latest_dir_path(self):
        try:
            dir_name=os.listdir(self.model_registry)
            if len(dir_name)==0:
                return None
            dir_name=list(map(int,dir_name))
            latest_dir_name=max(dir_name)
            return os.path.join(self.model_registry,latest_dir_name)
        except Exception as e:
            raise SensorException(e,sys)

    def get_latest_model_path(self):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                return Exception("Model is not found")
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
    

        except Exception as e:
            raise SensorException(e,sys)

    def get_latest_transformer_path(self):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                return Exception("Transformer is not found")
            return os.path.join(latest_dir,self.tranformed_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            raise SensorException(e,sys)

    def get_latest_target_encoder_path(self):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                return Exception("Target encoder is not found")
            return os.path.join(latest_dir,self.tranformed_dir_name,TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise SensorException(e,sys)

        
    def get_latest_save_dir_path(self):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                return os.path.join(self.model_registry,f'{0}')
            latest_dir_num=int(os.path.join(os.path.basename(self.get_latest_dir_path())))
            return os.path.join(self.model_registry,f'{latest_dir_num+1}')
        except Exception as e:
            raise SensorException(e,sys)

    def get_latest_save_model_path(self):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
        except Exception as e:
            raise SensorException(e,sys)

    def get_latest_save_target_encoder_path(self):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.target_encoder_dir,TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise SensorException(e,sys)

    def get_latest_save_transformer_path(self):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.tranformed_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            raise SensorException(e,sys)