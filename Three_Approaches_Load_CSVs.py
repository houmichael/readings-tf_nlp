# Define the path to the CSV file
emails_file_path = 'c:\\bronto1\\data\\emails.csv'

# Loading the emails -> Approach 1.-> Read in the whole csv file as a string
with open(emails_file_path, 'r') as emails_file:
    emails_str = emails_file.read() 


# Loading the emails -> Approach 2.->With PySpark
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Read the CSV file with header, handling multiline and escaping special characters
emails_spark_df = spark.read.format("csv"). \
        option("header", "true"). \
        option("multiLine", "true"). \
        option("escape", "\"").load(emails_file_path)

# Loading the emails -> Approach 3.->With Pandas
import pandas as pd
emails_pandas_df = pd.read_csv(emails_file_path)

