from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Define la función que será ejecutada por el PythonOperator
def print_hello_world():
    print("Hello, World!")

# Define el DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test',
    default_args=default_args,
    description='Un DAG simple de ejemplo',
    schedule_interval=timedelta(days=1),  # Ejecutar diariamente
    start_date=days_ago(1),               # Fecha de inicio del DAG
    catchup=False,                        # No ejecutar instancias pasadas
)

# Define las tareas
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

print_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello_world,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

# Define el orden de las tareas
start_task >> print_task >> end_task
