import pymongo
import pandas as pd
import json
import os
import sys
from dataclasses import dataclass
from dotenv import load_dotenv
print("Environment Variables is being called")
load_dotenv()

TARGET_COLUMN="class"

@dataclass
class EnvironmentVariable(object):
    mongodb_url:str=os.getenv("MONGODB_CREDENTIALS")
    aws_access_key:str=os.getenv("aws_access_key")
    aws_secret_key:str=os.getenv("aws_secret_key")

env_var=EnvironmentVariable()
mongo_client=pymongo.MongoClient(env_var.mongodb_url)