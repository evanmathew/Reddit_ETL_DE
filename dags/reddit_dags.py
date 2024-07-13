import sys
import os
from datetime import datetime
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

sys.path.insert(0,os.path.dirname((os.path.dirname(os.path.abspath(__file__))))) # insert parent directory (which will be the project root -REDDIT_D_E) into sys.path

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.upload_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'evan',
    'start_date': airflow.utils.dates.days_ago(2),
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# set file postfix to current date
# getting current date
file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    'etl_reddit_pipeline',
    default_args=default_args,
    description='Reddit ETL Pipeline',
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline'],
)

#extracting 100 post from reddit 
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline, # reddit_pipeline is a function in REDDIT_D_E/pipelines/reddit_pipeline.py
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
    
)


# uploading to s3 bucket
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline, # upload_s3_pipeline is a function in REDDIT_D_E/pipelines/upload_s3_pipeline.py
    dag=dag
)

extract >> upload_s3