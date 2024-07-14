# Reddit Data Engineering Project

## Overview

This project demonstrates a complete data pipeline for extracting, transforming, and loading (ETL) Reddit data into an Amazon Redshift data warehouse. The pipeline uses various AWS services and tools including Apache Airflow, PostgreSQL, AWS S3, AWS Glue, AWS Athena, and Amazon Redshift. The project is orchestrated using Docker and Apache Airflow to ensure a smooth workflow and ease of deployment.

## Architecture

### Data Source
- **Reddit API**: The source of the data. Reddit data is extracted using the Reddit API.

### Data Processing and Orchestration
- **Apache Airflow**: Used for orchestration of the data pipeline. Airflow manages the execution of tasks and ensures data flows through the pipeline.
- **PostgreSQL**: Used as the metadata database for Apache Airflow.
- **Celery**: Used for distributed task queueing to handle asynchronous tasks.
- **Docker**: Containers used for packaging and deploying the services.

### AWS Components
- **S3 Buckets**:
  - **Raw Storage**: Stores raw data from Reddit.
  - **Transformed Storage**: Stores transformed data ready for further processing and querying.
- **AWS Glue**:
  - **Data Catalog**: Maintains metadata of the datasets stored in S3.
  - **Crawlers**: Crawls data from S3 and populates the Data Catalog.
  - **ETL (Extract, Transform, Load)**: Transforms and loads data from S3 to Redshift.
- **Amazon Athena**: Used for querying data stored in S3 using SQL.
- **Amazon Redshift**: A data warehouse where the final transformed data is stored for analysis.
- **AWS IAM**: Manages access and permissions for AWS services.

### BI and Analytics Tools
- **Power BI**
- **Amazon QuickSight**
- **Tableau**
- **Looker Studio**

## Data Flow
1. **Extraction**: Reddit data is extracted using the Reddit API and saved to the raw storage S3 bucket.
2. **Transformation**: Data is processed using AWS Glue, transforming it into a structured format.
3. **Loading**: The transformed data is loaded into Amazon Redshift for analysis.

## Project Directory Structure

Reddit_D_E/

├── assets/

│   └── RedditDataEngineering.png

├── config/

│   └── config.conf.example

├── dags/
│   └── reddit_dag.py
├── data/
│   └── output/
│       └── reddit_20240712.csv
├── etls/
│   ├── aws_etl.py
│   └── reddit_etl.py
├── pipelines/
│   ├── aws_s3_pipeline.py
│   └── reddit_pipeline.py
├── utils/
│   └── constants.py
├── .gitignore
├── Dockerfile
├── README.md
├── airflow.env
├── docker-compose.yml
└── requirements.txt


