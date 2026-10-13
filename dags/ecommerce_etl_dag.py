from datetime import datetime, timedelta

# Light DAG definition representation compatible with standalone runners & tests
DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


class PipelineDAG:
    def __init__(self, dag_id: str, default_args: dict, schedule_interval: str):
        self.dag_id = dag_id
        self.default_args = default_args
        self.schedule_interval = schedule_interval
        self.tasks = []
        self.dependencies = {}

    def add_task(self, task_id: str) -> str:
        self.tasks.append(task_id)
        self.dependencies[task_id] = []
        return task_id

    def set_dependency(self, upstream: str, downstream: str) -> None:
        if downstream not in self.dependencies[upstream]:
            self.dependencies[upstream].append(downstream)


def create_ecommerce_dag() -> PipelineDAG:
    dag = PipelineDAG(
        dag_id="ecommerce_analytics_dbt_pipeline",
        default_args=DEFAULT_ARGS,
        schedule_interval="@daily",
    )

    t1 = dag.add_task("extract_raw_orders")
    t2 = dag.add_task("dbt_run_staging")
    t3 = dag.add_task("dbt_test_staging")
    t4 = dag.add_task("dbt_run_marts")
    t5 = dag.add_task("dbt_test_marts")
    t6 = dag.add_task("publish_analytics_metrics")

    dag.set_dependency(t1, t2)
    dag.set_dependency(t2, t3)
    dag.set_dependency(t3, t4)
    dag.set_dependency(t4, t5)
    dag.set_dependency(t5, t6)

    return dag
