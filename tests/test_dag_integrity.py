import unittest
from dags.ecommerce_etl_dag import create_ecommerce_dag


class TestDAGIntegrity(unittest.TestCase):
    def test_dag_structure_and_dependencies(self):
        dag = create_ecommerce_dag()
        self.assertEqual(dag.dag_id, "ecommerce_analytics_dbt_pipeline")
        self.assertEqual(len(dag.tasks), 6)

        # Check linear dependency flow
        self.assertIn("dbt_run_staging", dag.dependencies["extract_raw_orders"])
        self.assertIn("dbt_test_staging", dag.dependencies["dbt_run_staging"])
        self.assertIn("dbt_run_marts", dag.dependencies["dbt_test_staging"])
        self.assertIn("publish_analytics_metrics", dag.dependencies["dbt_test_marts"])


if __name__ == "__main__":
    unittest.main()
