from asyncio import tasks
import json
import pendulum
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_spast": False,
    "start_date": pendulum.datetime(2023, 1, 9),
    "email": ["rohanpatankar926@gmail.com"]
}


def training(**kwargs):
    from sensor.pipeline import simple_pipeline
    simple_pipeline.pipeline_inititate()

def sync_data_to_s3_bucket(**kwargs):
    bucket_name="sensorbucket98866"
    os.system(f"aws s3 sync /sensor/artifacts s3://{bucket_name}/artifacts/")
    os.system(f"aws s3 sync /sensor/saved_models s3://{bucket_name}/saved_models")

bash_success="echo 'Training Pipeline is completed successfully'"

with DAG(dag_id="training_dag",default_args=default_args,description="Sensor Training Pipeline",
schedule_interval="@weekly",catchup=False,tags=["sensor","something"]) as dag:   
    
    training_pipeline=PythonOperator(task_id="training_pipeline",python_callable=training)

    sync_data_2_s3_bucket=PythonOperator(task_id="sync_data_2_s3_bucket",python_callable=sync_data_to_s3_bucket)

    success=BashOperator(task_id="success",bash_command=bash_success)


    training_pipeline>>sync_data_2_s3_bucket>>success