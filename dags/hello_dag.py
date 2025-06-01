import time
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello from a Kubernetes Pod!")
    time.sleep(10)
    print("Again, hello from a Kubernetes Pod!")



with DAG("hello_kubernetes",
         start_date=datetime(2024, 1, 1),
         schedule_interval=None,
         catchup=False) as dag:
    PythonOperator(
        task_id="hello_task",
        python_callable=hello
    )
