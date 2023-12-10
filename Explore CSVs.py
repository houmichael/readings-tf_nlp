# Loading the emails -> Approach 2.->With PySpark
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Define the path to the CSV file
emails_file_path = 'c:\\bronto1\\data\\emails.csv'

# Read the CSV file with header, handling multiline and escaping special characters
emails_spark_df = spark.read.format("csv"). \
        option("header", "true"). \
        option("multiLine", "true"). \
        option("escape", "\"").load(emails_file_path)

# Loading the emails -> Approach 3.->With Pandas
import pandas as pd
emails_pandas_df = pd.read_csv(emails_file_path)
