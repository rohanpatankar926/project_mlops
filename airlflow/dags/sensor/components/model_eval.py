import sys
import os
sys.path.append(os.getcwd())
from sensor.predictor import ModelResolver
from sensor.entity import config_entity
from sensor.entity import artifacts_entity
from sensor.logger import logging
from sensor.utils import load_object
from sklearn.metrics import f1_score
import pandas as pd

from sensor.config import TARGET_COLUMN
from sensor.exception import SensorException

class ModelEvaluation(object):
    def __init__(self,
    model_eval_config:config_entity.ModelEvaluationConfig,
    data_ingestion_artifact:artifacts_entity.DataIngestionArtifact,
    data_trasnformation_artifact:artifacts_entity.DataTransformationArtifact,
    model_trainer_artifact:artifacts_entity.ModelTrainerArtifact
    ):
        try:
            logging.info(f"{'>>>'*20} Model Evaluation {'<<<'*20}")
            self.model_eval_config=model_eval_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_transformation_artifact=data_trasnformation_artifact
            self.model_trainer_artifact=model_trainer_artifact
            self.model_resolver=ModelResolver()
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_evaluation(self):
        try:
            logging.info("If saved model folder has model then we will compare which model is best trained or the model from the saved model folder")
            latest_dir_path=self.model_resolver.get_latest_dir_path()
            if latest_dir_path == None:
                model_eval_artifact=artifacts_entity.ModelEvaluatorArtifact(is_model_accepted=True,improved_accuracy=None)
                logging.info(f"mode evaluation artifact is created {model_eval_artifact}")
                return model_eval_artifact
            logging.info(f"Finding location of transformer,model and target encoder")
            transformer_path=self.model_resolver.get_latest_transformer_path()
            model_path=self.model_resolver.get_latest_model_path()
            target_encoder_path=self.model_resolver.get_latest_target_encoder_path()
            logging.info("Previous trained model,tranformer,target is loaded")
            transformer=load_object(transformer_path)
            model=load_object(model_path)
            target_encoder=load_object(target_encoder_path)
            logging.info("Previous trained model,tranformer,target is loaded")
            current_transformer=load_object(self.data_transformation_artifact.transformed_object_path)
            current_model=load_object(self.model_trainer_artifact.model_path)
            current_target_encoder=load_object(self.data_transformation_artifact.target_encoder_path)
            test_df=pd.read_csv(self.data_ingestion_artifact.test_file_path)
            target_df=test_df[TARGET_COLUMN]
            
            #previous model
            y_true=transformer.transform(target_df)
            input_feature_name=list(transformer.feature_names_in_)
            input_arr=transformer.transform(test_df[input_feature_name])
            y_pred=model.predict(input_arr)
            print(f"y_true-->{y_true}")
            previous_model_score=f1_score(y_true,y_pred,average='weighted')
            logging.info(f"Previous model score is {previous_model_score}")

            #current model
            y_true=target_encoder.transform(target_df)
            print(f"y_true-->{y_true}")
            print(f"Prediction using trained model-->{current_target_encoder.inverse_transform(y_pred)[:5]}")
            current_model_score=f1_score(y_true,y_pred,average='weighted')
            logging.info(f"Current model score is {current_model_score}")
            if current_model_score==previous_model_score:
                logging.info("Model is not accepted since the score is same")
                raise Exception("Model is not accepted since the score is same")
            if current_model_score<=previous_model_score:
                logging.info("Model is not accepted since the score is less than previous model")
                raise Exception("Model is not accepted since the score is less than previous model")
            model_eval_artifact=artifacts_entity.ModelEvaluatorArtifact(is_model_accepted=True,improved_accuracy=current_model_score-previous_model_score)
            difference_score=current_model_score-previous_model_score
            print(difference_score)
            logging.info(f"model_eval_artifact is created {model_eval_artifact}")
        except Exception as e:
            raise SensorException(e,sys)