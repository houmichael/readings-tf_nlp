import sys, os, re, email
from collections import Counter
import nltk
from nltk.corpus import stopwords

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


# Find the nth occurrence of a substring in a string
# the text between the two occurrences of the substring is returned
def find_nth_occurrence_text(main_string, substring, n):
    start = main_string.find(substring)
    while start != -1 and n > 1:
        start = main_string.find(substring, start + 1)
        n -= 1

    if start != -1:
        end = main_string.find(substring, start + len(substring))
        if end != -1:
            return ("\""+substring+main_string[start + len(substring):end])[:-2]
    
    return None

# First row of the csv file, which is for the first email
row1 = find_nth_occurrence_text(emails_str, "allen-p/", 1)

# The 10th row of the csv file, which is for the 10th email
row10 = find_nth_occurrence_text(emails_str, "allen-p/", 10)

# Now let's use the 10th row to explore the email
email.message_from_string(row10.split("\",\"")[1]).get_payload()
email_10 = email.message_from_string(row10.split("\",\"")[1])
message_10 = email_10.get_payload()

nltk.download('stopwords')
stopwords = stopwords.words('english')

message_10_cleaned = re.sub(" +", " ",re.sub(r"[\W\d]|--"," ", message_10)).strip().lower().split(" ")

message_10_no_stopwords = [x for x in message_10_cleaned if x not in stopwords]

message_10_freq = sorted(dict(Counter(message_10_cleaned)).items(), key=lambda x: x[1], reverse=True)

