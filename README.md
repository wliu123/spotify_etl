## Spotify ETL Project

# Table of Contents
* [Project Overview](#project-overview)
* [ETL Pipeline](#etl-pipeline)
* [AWS Resources](#aws-resources)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

# Project Overview
The purpose of this project is to create a comprehensive ETL (Extract, Transform, Load) pipeline for processing data from the Spotify API. The pipeline leverages AWS resources and Python as the primary runtime language to ensure seamless data extraction, transformation, and loading.
The flow diagram is below:

![Screenshot 2023-11-03 at 11 38 16 PM](https://github.com/wliu123/spotify_etl/assets/59156681/bf574254-9b36-4720-8dd3-3fb431c21001)

# ETL Pipeline
The ETL pipeline is designed to handle data flow from end to end:

1. Data Extraction: AWS Lambda function with Python as the runtime language is used to extract data from the Spotify API and store within the raw_data folder in a S3 bucket. To have the extraction provided on a regular cadence, the use of Cloudwatch events would be able to create this trigger. Developer account is needed to access the API utilizing your personal clientID and secret. Register for the API here: https://developer.spotify.com/. For this project, I decided to pull data from a Spotify created playlist detailing the top songs globally.

2. Data Transformation: When a file is placed in the raw_data folder, another AWS Lambda function is triggered to transform the data. This transformation involves converting the raw JSON file into a structured dataframe and organizing it in a way suitable for database ingestion with the correct data types and ready for ingestion into datawarehouse tables. The processed files are generated within the transformed_data folder and the original file is moved from the raw_file folder to the processed_file folder.

3. Data Loading: Within the transformed_data folder, there are 3 additional folders to hold the transformed table for each dataset. Snowflake Snowpipe is configured to auto-ingest new files in CSV format directly into the tables within the Snowflake data warehouse. This final step ensures that the data is prepped for use in data visualizations or other analytical tasks.

# AWS Resources
This project relies on the following AWS resources:

* AWS Cloudwatch: Used for scheduling data extraction intervals.
* AWS Lambda: Used for data extraction and transformation.
* Amazon S3: Serves as the storage for raw and transformed data.
* AWS IAM: Grants the appropriate roles to each AWS service to allow for them to communicate with one another.
* Snowflake Snowpipe: Facilitates automated data loading into the data warehouse.

# Usage
To use this ETL pipeline for your Spotify data:

1. Set up the required AWS resources, including AWS Lambda functions and S3 buckets.
2. Configure the Spotify API integration.
3. Deploy the ETL pipeline code using Python and AWS Lambda functions.
4. Monitor the pipeline's performance and data flow.
5. Setup Snowpipe with Snowflake to auto ingest data from the appropriate endpoint in AWS
6. Monitor the appropriate tables within Snowflake to ensure data was retrieved properly
   
For more detailed instructions and code samples, refer to the project's code repository.

# Contributing
Contributions to this project are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Your input and enhancements are appreciated.

# License
This project is licensed under the MIT License.

Enjoy my Spotify ETL project, and may it provide valuable insights and data for your music and analytical needs!
