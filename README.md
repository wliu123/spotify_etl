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

I start out by connecting to the spotify API which requires a Spotify Developers account as you will need a clientID and secret in order to access their API. Register for the API here: https://developer.spotify.com/
Take some time to get familiar with the documentation and what kind of data you'll be able to pull. For this project, I decided to pull data from a Spotify created playlist detailing the top songs globally. Within AWS, I can test
the Lambda function I created to extract the JSON data and convert it into a format that's readable i.e: csv or I can schedule within Cloudwatch how often I'd like the Lambda function to be triggered. I opted to just manually test it out
for developmental purposes. 

The Lambda function extracts the data and inserts it into a raw_data folder located within a s3 bucket. The s3 bucket also contains a transformed_data file where my processed data will live. I utilize another Lambda function to do the
transformation process by creating a trigger for when a file is inserted into the raw_data file, I autonomously clean the data of any duplicates and null values, clean the data types, and extract only the information I want to place within my
tables. Tables live in Snowflake and I have 3 different snowpipes configured to watch the 3 folders living within the transformed_data folder and once again, extract the transformed data directly to my tables within Snowflake.

From there, if I wanted to create any insights within a data visualization tool such as PowerBI or Tableau, processed clean data is already properly stored within my datawarehouse.




 

ETL Pipeline
The ETL pipeline is designed to handle data flow from end to end:

Data Extraction: AWS Lambda functions are used to extract data from the Spotify API. The raw data is stored in the raw_data folder within an S3 bucket.

Data Transformation: When a file is placed in the raw_data folder, another AWS Lambda function is triggered to transform the data. This transformation involves converting the raw JSON file into a structured dataframe and organizing it in a way suitable for database ingestion. The processed file is then moved to the transformed_data folder.

Data Loading: In the transformed_data folder, Snowflake Snowpipe is configured to auto-ingest new files in CSV format directly into the tables within the Snowflake data warehouse. This final step ensures that the data is prepped for use in data visualizations or other analytical tasks.

AWS Resources
This project relies on the following AWS resources:

AWS Lambda: Used for data extraction and transformation.
Amazon S3: Serves as the storage for raw and transformed data.
Snowflake Snowpipe: Facilitates automated data loading into the data warehouse.
Usage
To use this ETL pipeline for your Spotify data:

Set up the required AWS resources, including AWS Lambda functions and S3 buckets.
Configure the Spotify API integration.
Deploy the ETL pipeline code using Python and AWS Lambda functions.
Monitor the pipeline's performance and data flow.
For more detailed instructions and code samples, refer to the project's code repository.

Contributing
Contributions to this project are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Your input and enhancements are appreciated.

License
This project is licensed under the MIT License.

Enjoy your Spotify ETL project, and may it provide valuable insights and data for your analytical needs!
