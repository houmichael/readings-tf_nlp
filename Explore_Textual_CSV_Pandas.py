# Define the path to the CSV file
emails_file_path = 'c:\\bronto1\\data\\emails.csv'

# Loading the emails -> Approach 3.->With Pandas
import pandas as pd
emails = pd.read_csv(emails_file_path)

