from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifacts_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
from sklearn.pipeline import Pipeline
import pandas as pd
from sensor import utils
from sklearn.preprocessing import LabelEncoder
from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.preprocessing import RobustScaler
from sensor.config import TARGET_COLUMN

class DataTransformation:
    def __init__(self,transormation_config:config_entity.DataTransformationConfig,
                    data_ingestion_artifacts:artifacts_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>>'*20} Data Transformation {'<<<'*20}")
            self.data_transformation_config=transormation_config
            self.data_ingestion_artifacts=data_ingestion_artifacts
        except Exception as e:
            raise SensorException(e, sys)

    @classmethod
    def get_data_transformation_object(cls):
        try:
            simple_imputer=SimpleImputer(strategy="constant",fill_value=0)
            robust_scaler=RobustScaler()
            pipeline=Pipeline(steps=[("imputer",simple_imputer),("robust_scaler",robust_scaler)])
            return pipeline
        except Exception as e:
            raise SensorException(e, sys)
    
    def initiate_data_transformation(self):
        try:
            train_df=pd.read_csv(self.data_ingestion_artifacts.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifacts.test_file_path)

            #select the input features for the train and test df independent 
            input_feature_train_df=train_df.drop(TARGET_COLUMN,axis=1)
            input_feature_test_df=test_df.drop(TARGET_COLUMN,axis=1)
            #select the input features for the train and test df dependent 
            target_feature_train_df=train_df[TARGET_COLUMN]
            target_feature_test_df=test_df[TARGET_COLUMN]

            label_encoder=LabelEncoder()
            label_encoder.fit(target_feature_train_df)

            target_feature_train_arr=label_encoder.transform(target_feature_train_df)
            target_feature_test_arr=label_encoder.transform(target_feature_test_df)

            transformation_pipeline=DataTransformation.get_data_transformation_object()
            transformation_pipeline.fit(input_feature_train_df)
            
            input_feature_train_arr=transformation_pipeline.transform(input_feature_train_df)
            input_feature_test_arr=transformation_pipeline.transform(input_feature_test_df)

            smote_tomek=SMOTETomek()
            logging.info("before resampling in training set Input Feature Shape: {}, target shape :{}".format(input_feature_train_arr.shape,target_feature_train_arr.shape))
            input_feature_train_arr,target_feature_train_arr=smote_tomek.fit_resample(input_feature_train_arr,target_feature_train_arr)
            logging.info("After resampling in training set Input Feature Shape: {},target shape: {}".format(input_feature_train_arr.shape,target_feature_train_arr.shape))
           
            logging.info("before resampling in testing set Input Feature Shape: {}, target shape :{}".format(input_feature_test_arr.shape,target_feature_test_arr.shape))
            input_feature_test_arr,target_feature_test_arr=smote_tomek.fit_resample(input_feature_test_arr,target_feature_test_arr)
            logging.info("After resampling in testing set Input Feature Shape: {},target shape: {}".format(input_feature_test_arr.shape,target_feature_test_arr.shape))

            train_arr=np.c_[input_feature_train_arr,target_feature_train_arr]
            test_arr=np.c_[input_feature_test_arr,target_feature_test_arr]

            utils.save_numpy_array_data(file_path=self.data_transformation_config.tranformed_train_path,data=train_arr)
            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_test_path,data=test_arr)

            utils.save_object(model=self.data_transformation_config.transform_object_path,obj=transformation_pipeline)
            utils.save_object(model=self.data_transformation_config.target_encoder_path,obj=label_encoder)


            data_tranformation_artifacts=artifacts_entity.DataTransformationArtifact(
                    transformed_object_path=self.data_transformation_config.transform_object_path,
                    transformed_train_path=self.data_transformation_config.tranformed_train_path,
                    transformed_test_path=self.data_transformation_config.transformed_test_path,
                    target_encoder_path=self.data_transformation_config.target_encoder_path)
            logging.info(f"Data Transformation pipeline Completed --> {data_tranformation_artifacts}")
            return data_tranformation_artifacts
        except Exception as e:
            raise SensorException(e, sys)