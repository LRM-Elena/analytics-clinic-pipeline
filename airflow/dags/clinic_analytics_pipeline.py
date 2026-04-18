from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# DAG default configuration
default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email": ["rmli020107@gmail.com"],     
    "email_on_failure": True,                       # alert on real failure
    "email_on_retry": False,                        # don't alert on retry attempts
}

# Define the DAG
with DAG(
    dag_id="analytics_clinic_dbt_pipeline",
    description="Run dbt models for Analytics Clinic project",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='0 2 * * *',                              # Daily at 2 AM
    catchup=False,
    tags=["dbt", "analytics_clinic"],
) as dag:

    # # Install dbt dependencies
    # dbt_deps = BashOperator(
    #     task_id='dbt_deps',
    #     bash_command='cd /opt/airflow/dbt/clinic_dbt && dbt deps --profiles-dir /opt/airflow/config',
    # )

    # Run dbt staging
    run_dbt_staging = BashOperator(
        task_id='dbt_run_staging',
        bash_command='cd /opt/airflow/dbt/clinic_dbt && dbt run --select staging',
    )
    
    # Run dbt intermediate
    run_dbt_intermediate = BashOperator(
        task_id='dbt_run_intermediate',
        bash_command='cd /opt/airflow/dbt/clinic_dbt && dbt run --select intermediate',
    )
    
    # Run dbt marts
    run_dbt_marts = BashOperator(
        task_id='dbt_run_marts',
        bash_command='cd /opt/airflow/dbt/clinic_dbt && dbt run --select marts',
    )
    
    # Test dbt models
    test_dbt = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt/clinic_dbt && dbt test',
    )
    
    # Define dependencies
    # dbt_deps >> run_dbt_staging >> run_dbt_intermediate >> run_dbt_marts >> test_dbt
    run_dbt_staging >> run_dbt_intermediate >> run_dbt_marts >> test_dbt




    # # Phase 1: Use echo commands to verify DAG structure
    
    # test_dbt_version = BashOperator(
    #     task_id='test_dbt_version',
    #     bash_command='echo "Step 1: Testing dbt installation"',
    # )
    
    # run_dbt_staging = BashOperator(
    #     task_id='dbt_run_staging',
    #     bash_command='echo "Step 2: Running dbt staging models"',
    # )
    
    # run_dbt_intermediate = BashOperator(
    #     task_id='dbt_run_intermediate',
    #     bash_command='echo "Step 3: Running dbt intermediate models"',
    # )
    
    # run_dbt_marts = BashOperator(
    #     task_id='dbt_run_marts',
    #     bash_command='echo "Step 4: Running dbt marts models"',
    # )
    
    # test_dbt_models = BashOperator(
    #     task_id='dbt_test',
    #     bash_command='echo "Step 5: Testing dbt models"',
    # )
    
    # # Define dependencies
    # test_dbt_version >> run_dbt_staging >> run_dbt_intermediate >> run_dbt_marts >> test_dbt_models