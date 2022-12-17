import pandas as pd
import os,sys
sys.path.append(os.getcwd())
from sensor.logger import logging
from sensor.config import mongo_client
from sensor.exception import SensorException

def get_collection_as_dataframe(database_name:str,collection_name:str):
    '''
    Description: This function is used to get the collection as dataframe from the MongoDB
    ============================================
    Input: database_name:str,collection_name:str
    Output: dataframe
    =============================================
    return pandas dataframe
    '''
    try:
        logging.info(f"Reading the data from the database from MongoDB --> database name-->[{database_name}] ,collection name-->[{collection_name}]")
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Data loaded from MongoDB successfully with rows {df.shape[0]} and columns {df.shape[1]}")
        if "_id" in df.columns:
            logging.info("dropping the _id column")
            df.drop("_id",axis=1,inplace=True)
            logging.info("Dropped the _id column successfully")
        return df
    except Exception as e:
        raise SensorException(e,sys)