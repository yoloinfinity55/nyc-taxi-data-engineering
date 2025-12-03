from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import os

# Automatically get the project root based on AIRFLOW_HOME
PROJECT_ROOT = os.environ.get("AIRFLOW_HOME")

default_args = {
    'owner': 'minijohn',
    'start_date': days_ago(1),
    'catchup': False,
}

with DAG(
    dag_id='nyc_taxi_elt_pipeline',
    default_args=default_args,
    schedule_interval='@monthly',
) as dag:

    # 1. Ingest
    ingest_task = BashOperator(
        task_id='ingest_data',
        bash_command=f'python3 {PROJECT_ROOT}/scripts/ingest.py'
    )

    # 2. Transform
    # Note: We must be inside the dbt project folder to run dbt
    transform_task = BashOperator(
        task_id='dbt_build',
        bash_command=f'cd {PROJECT_ROOT}/dbt/taxi_transform && dbt build'
    )

    ingest_task >> transform_task
