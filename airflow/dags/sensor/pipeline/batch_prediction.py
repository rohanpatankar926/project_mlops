from sensor.exception import SensorException
from sensor.logger import logging
from sensor.predictor import ModelResolver
import sys
import os
from sensor.utils import load_object
import pandas as pd
import numpy as np
from datetime import datetime

PREDICTION_DIR = "prediction"

def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR, exist_ok=True)
        logging.info("Starting the batch prediction")
        model_resolver = ModelResolver(model_registry="saved_models")
        logging.info("reading the data")
        df=pd.read_csv(input_file_path)
        df.replace({"na":np.NAN},inplace=True)

        #validation
        transformer=load_object(file_path=model_resolver.get_latest_transformer_path())
        input_feature_name=list(transformer.feature_names_in_)
        input_arr=transformer.transform(df[input_feature_name])

        logging.info("converting categorical target class to numerical class")
        model=load_object(file_path=model_resolver.get_latest_model_path())
        prediction=model.predict(input_arr)
        target_encoder=load_object(file_path=model_resolver.get_latest_target_encoder_path())
        cat_predicition=target_encoder.inverse_transform(prediction)

        df["prediction"]=prediction
        df["cat_prediction"]=cat_predicition

        prediction_file_name=os.path.basename(input_file_path).replace(".csv",f"_{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
        return prediction_file_name
    except Exception as e:
        raise SensorException(e,sys)