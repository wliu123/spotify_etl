# Spotify_ETL 

The purpose of this project is to create an ETL pipeline from end to end. I will be using AWS resources along with Python as the main runtime language. 
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
