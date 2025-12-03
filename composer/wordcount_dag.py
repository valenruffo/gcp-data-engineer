from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from datetime import datetime

default_args = {
    'owner': 'data-engineer',
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

dag = DAG(
    'wordcount_dataflow',
    default_args=default_args,
    description="Ejecutar job de Dataflow desde template",
    schedule_interval="@daily",
    catchup=False
) 
    
dataflow_task = DataflowTemplatedJobStartOperator(
    task_id="ejecutar_wordcount",
    template='gs://gcs-bucket-06/templates/wordcount_template',
    parameters={
        'input': 'gs://gcs-bucket-06/data/input.txt',
        'output': 'gs://gcs-bucket-06/data/output'
    },
    location='us-central1',
    project_id='gcp-data-engineer-05',
    dag=dag
)