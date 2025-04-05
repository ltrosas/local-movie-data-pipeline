#test
#test2
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "ltrosas",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="movie_etl_pipeline",
    default_args=default_args,
    description="A simple ETL pipeline with local Postgres and dbt",
    schedule_interval=None, 
    catchup=False,
) as dag:

    load_csv_to_postgres = BashOperator(
        task_id="load_csv_to_postgres",
        bash_command="source ../venv/bin/activate && python ../../load_data.py"
    )

    run_dbt_models = BashOperator(
        task_id="run_dbt_models",
        bash_command="cd ../../dbt/local_movie_data_pipeline && dbt run"
    )

    load_csv_to_postgres >> run_dbt_models
