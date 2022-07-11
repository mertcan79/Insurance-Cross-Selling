# Insurance Cross Selling ETL Pipeline

An Insurance company that provides health insurance to its customers offers other insurance product to the customers through diffirent kind of marketing channels.A model is built to predict whether the customers will also be interested in vehicle insurance provided by the same company.

## Some of the Business Questions

1. How does the age of a vehicle determine the response of vehicle insurance advertisment?
2. How to attract customers from different generation?
3. What are the major factors that make a health insurance customer not intersted with vehicle insurance?
4. Can an ML model be used to predict the user likeliness of buying vehicle insurance?

A data pipeline is created to upload Insurance data to S3 & Redshfit, connect to the warehouse and perform EDA & build an ML model. 

## Architecture

1. Extract data from the source
2. Load into [AWS S3](https://aws.amazon.com/s3/)
3. Copy into [AWS Redshift](https://aws.amazon.com/redshift/)
4. Create Jupyter Dashboard 
1. Orchestrate with [Airflow](https://airflow.apache.org) in [Docker](https://www.docker.com)
1. Create AWS resources with [Terraform](https://www.terraform.io)

## Output

1. The first output is an .ipynb file containing conclusions and recommendations from the insights gathered from the EDA.ipynb and the evaluation of the ML models built.

2. The second output comes from a .py file which takes a test dataset and performs the ML operations to create a .csv of predictions.

> **NOTE**: This was developed using a Windows. If you're on Mac or Linux, you may need to amend certain components if issues are encountered.
