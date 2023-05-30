from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifacts_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
from xgboost import XGBClassifier
from sensor import utils 
from sklearn.metrics import f1_score

def fine_tune():
    try:
        #fine tune the modesl using grid search
        pass
    except Exception as e:
        raise SensorException(e,sys)

class ModelTrainer:
    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig,
                    data_trasformation_artifact:artifacts_entity.DataTransformationArtifact):
        try:
            logging.info(f"{'>>'*20} Model Trainer Initiated {'<<'*20}")
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_trasformation_artifact
        except Exception as e:
            raise SensorException(e,sys) 

    
    def train_model(self,x,y):
        try:
            xgb_clf=XGBClassifier()
            xgb_clf.fit(x,y)
            return xgb_clf
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_trainer(self):
        try:
            logging.info("loading train and test array")
            train_arr=utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr=utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)
            logging.info("loading train and test array completed")
            x_train,y_train=train_arr[:,:-1],train_arr[:,-1]
            x_test,y_test=test_arr[:,:-1],test_arr[:,-1]
            logging.info("training the model")
            model=self.train_model(x=x_train,y=y_train)
            logging.info("training the model completed")
            yhat_test=model.predict(x_test)
            f1_score_test=f1_score(y_test,yhat_test,average="weighted")
            yhat_train=model.predict(x_train)
            f1_score_train=f1_score(y_train,yhat_train)
            logging.info(f"f1 score for test data is {f1_score_test}")
            
            logging.info("Checking if my model is overfitting or not")
            if f1_score_test<self.model_trainer_config.expected_score:
                raise Exception("model overfitting and is not able to meet our expected results --> expected_accuracy: {self.model_trainer_config.expected_score} and actual_accuracy: {f1_score_test}")
            diff=abs(f1_score_test-f1_score_train)
            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception("model overfitting and is not able to meet our expected results --> expected_accuracy: {self.model_trainer_config.expected_score} and actual_accuracy: {f1_score_test}")
            logging.info("saving the object model")
            utils.save_object(model=self.model_trainer_config.model_path,obj=model)
            logging.info("saving the object model completed")
            model_trainer_artifact=artifacts_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path,
                                                                        f1_score_test=f1_score_test,
                                                                        f1_score_train=f1_score_train)
            logging.info("Model Trainer artifact --> {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)
        

