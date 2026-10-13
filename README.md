# 🏗️ Airflow dbt Pipeline

[![CI Pipeline](https://github.com/MSBHOSLE/airflow-dbt-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/MSBHOSLE/airflow-dbt-pipeline/actions)
[![Apache Airflow](https://img.shields.io/badge/Airflow-2.8%2B-017CEE?logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
[![dbt](https://img.shields.io/badge/dbt-Core%201.7-FF694B?logo=dbt&logoColor=white)](https://getdbt.com/)
[![SQL](https://img.shields.io/badge/SQL-Transformations-orange?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise **orchestrated data warehouse transformation pipeline** linking **Apache Airflow** DAG orchestration with **dbt** (data build tool) modeling, testing, and continuous quality checks.

---

## 🏗️ DAG Workflow

```mermaid
flowchart LR
    Extract["📥 extract_raw_orders"] --> StagingRun["⚙️ dbt_run_staging"]
    StagingRun --> StagingTest["🧪 dbt_test_staging"]
    StagingTest --> MartsRun["⚙️ dbt_run_marts"]
    MartsRun --> MartsTest["🧪 dbt_test_marts"]
    MartsTest --> Publish["📊 publish_analytics_metrics"]
```

---

## ⚡ Highlights

- **Linear DAG Orchestration**: Explicit task dependencies with automated retry policies.
- **dbt Testing & Validation**: Automated uniqueness, not-null, and dimensional consistency checks before publication to production marts.
- **Clean Staging & Dimensional Marts**: Staging views cleansing source raw tables into standardized fact & dimension tables.

---

## 🚀 Running DAG Tests

```bash
python -m unittest discover tests
```

---

## 👤 Author

**Mahesh Sanjayrao Bhosle**
- **GitHub:** [@MSBHOSLE](https://github.com/MSBHOSLE)
- **LinkedIn:** [Mahesh Bhosle](https://linkedin.com/in/mahesh-bhosle-916991198)
- **Email:** msbhosle.2@gmail.com
- **Education:** M.Sc. Data & Computer Science, Heidelberg University

---

## 📄 License

MIT License - see [LICENSE](LICENSE).
