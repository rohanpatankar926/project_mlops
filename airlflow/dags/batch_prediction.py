from asyncio import tasks
import json
import pendulum
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def download_files(**kwargs):
    global bucket_name
    bucket_name="sensor-data"
    global input_dir
    input_dir="/sensor/input_files"
    os.makedirs(input_dir,exist_ok=True)
    os.system(f"aws s3 sync s3://{bucket_name}/input_files /sensor/input_files")

def batch_prediction(**kwargs):
    from sensor.pipeline import batch_pred
    for file_name in os.listdir(input_dir):
        batch_pred.start_batch_data_predsiction(input_file_path=os.path.join(input_dir,file_name))

def sync_prediction_to_s3_bucket(**kwargs):
    os.system(f"aws s3 sync /sensor/prediction s3://{bucket_name}/prediction")

bash_success="echo 'Batch Prediction is completed successfully'"

with DAG(
    'sensor_training',
    default_args={'retries': 2},
    # [END default_args]
    description='Sensor Fault Detection',
    schedule_interval="@weekly",
    start_date=pendulum.datetime(2023, 1, 9, tz="UTC"),
    catchup=False,
    tags=['sensor','batch_prediction'],
) as batch_pred_dag:

    download_input_files=PythonOperator(task_id="download_input_files",python_callable=download_files)

    generate_prediction_files=PythonOperator(task_id="generate_prediction_files",python_callable=batch_prediction)

    sync_prediction_files=PythonOperator(task_id="sync_prediction_files",python_callable=sync_prediction_to_s3_bucket)
    
    success=BashOperator(task_id="success",bash_command=bash_success)

    download_input_files>>generate_prediction_files>>sync_prediction_files>>success
