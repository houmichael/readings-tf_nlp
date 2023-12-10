import sys, os
from collections import Counter

# Define the path to the CSV file
emails_file_path = 'c:\\bronto1\\data\\emails.csv'

# Loading the emails -> Approach 1.-> Read in the whole csv file as a string
with open(emails_file_path, 'r', encoding='utf-8') as emails_file:
    emails_str = emails_file.read()

emails_str[:1000]
len(emails_str)

# Get an estimate of memory usage of the string
emails_str_memory = sys.getsizeof(emails_str)
# Get an estimate of disk usage of the string when it is saved
emails_str_disk = os.path.getsize(emails_file_path)/(1024**3)
print(f"Memory Usage is about: {emails_str_memory}")
print(f"Disk USage is about: {emails_str_disk}")
# Memory Usage is about: 2852243730
# Disk USage is about: 1.3281798167154193

