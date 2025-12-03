# NYC Taxi ELT Pipeline (Airflow + dbt + DuckDB)

## 🚀 Project Overview
A local-first, scalable ELT (Extract, Load, Transform) pipeline that processes NYC Taxi data using the modern data stack.
Designed to be highly performant on local hardware (Mac M1) while simulating a production-grade cloud architecture.

**Architecture:**
*   **Orchestration:** Apache Airflow (Local Executor)
*   **Transformation:** dbt Core (Data Build Tool)
*   **Storage/Compute:** DuckDB (OLAP Database) + Parquet (Data Lake)
*   **Language:** Python 3.11 + SQL

## 🏗️ Architecture Diagram
`[Ingest Script] -> [Raw Parquet (Data Lake)] -> [DuckDB] -> [dbt Models (Bronze/Silver/Gold)] -> [Analytics]`

## 🔧 Pipeline Steps
1.  **Ingestion:** Python script streams large Parquet files from NYC TLC public S3 buckets.
2.  **Storage:** Raw data is stored in a local Data Lake (partitioned by month/year).
3.  **Staging (Bronze):** dbt reads Parquet files directly using DuckDB's `read_parquet` for zero-copy ingestion.
4.  **Mart (Gold):** Aggregated revenue metrics by payment type and distance.

## 🛠️ Setup & Usage

### 1. Prerequisites
*   Python 3.11+
*   DuckDB

### 2. Installation
```bash
# Clone repository
git clone <repo-url>
cd nyc_taxi_portfolio

# Create Virtual Environment
python3.11 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
