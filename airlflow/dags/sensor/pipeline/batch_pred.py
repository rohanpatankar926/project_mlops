from sensor.predictor import ModelResolver
from sensor.utils import *
import os
import numpy as np
import pandas as pd

from datetime import datetime
PREDICTION_DIR="prediction"
def start_batch_data_predsiction(input_file_path):
    os.makedirs(PREDICTION_DIR,exist_ok=True)
    model_resolver=ModelResolver(model_registry="saved-models")
    df=pd.read_csv(input_file_path) 
    df.replace({"na":np.NaN},inplace=True)

    transformer=load_object(file_path=model_resolver.get_latest_transformer_path())
    input_feature_names=list(transformer.feature_names_in_)
    input_arr=transformer.transform(df[input_feature_names])

    model=load_object(file_path=model_resolver.get_latest_model_path())
    prediction=model.predict(input_arr)
    target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())

    cat_prediction = target_encoder.inverse_transform(prediction)
    df["prediction"]=prediction
    df["cat_pred"]=cat_prediction

    prediction_file_name=os.path.basename(input_file_path).replace(".csv",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
    prediction_file_path=os.path.join(PREDICTION_DIR,prediction_file_name)
    df.to_csv(prediction_file_path,index=False,header=True)
    return prediction_file_path
