import sys, os, re, email
from collections import Counter
from Stopwords import stop_nltk, stop_cwf, stop_iso, stop_smart

# Define the path to the CSV file
emails_file_path = 'c:\\bronto1\\data\\emails.csv'

email_indicator = "\"Message-ID:"

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
def find_nth_email(main_string, substring, n):
    start = main_string.find(substring)
    while start != -1 and n > 1:
        start = main_string.find(substring, start + 1)
        n -= 1

    if start != -1:
        end = main_string.find("\"\n", start + 1)
        if end != -1:
            return ("\""+substring+main_string[start + len(substring):end])
    
    return None


# Extracts all email addresses from a given string based on a specified indicator.
def extract_emails(emails_str, indicator, n):
    email = find_nth_email(emails_str, indicator, n)
    emails =[]
    
    while email != None:
        email = emails.append(email)
        if n == len(emails):
            return emails
        email = find_nth_email(emails_str, indicator, n)
    
    return emails

# Extracts all email addresses from a given string based on a specified indicator.
def extract_all_emails(emails_str, indicator):
    n = 1
    email = find_nth_email(emails_str, indicator, n)
    emails =[]
    
    while email != None:
        email = emails.append(email)
        print(f"number of emails extracted: {len(emails)}")
        n += 1
        email = find_nth_email(emails_str, indicator, n)
    
    return emails

extract_emails(emails_str, email_indicator, 1)

# extract_all_emails(emails_str, email_indicator)

# First row of the csv file, which is for the first email
row1 = find_nth_email(emails_str, email_indicator, 1)

# The 10th row of the csv file, which is for the 10th email
row10 = find_nth_email(emails_str, email_indicator, 10)

# Now let's use the 10th row to explore the email
email10 = email.message_from_string(row10)
message10 = email10.get_payload()

message10_cleaned = re.sub(" +", " ",re.sub(r"[\W\d]|--"," ", message10)).strip().lower().split(" ")
message10_freq = sorted(dict(Counter(message10_cleaned)).items(), key=lambda x: x[1], reverse=True)
message10_freq[:25]

message10_cleaned_stop = [x for x in message10_cleaned if x not in stop_smart]
message10_freq_stop = sorted(dict(Counter(message10_cleaned_stop)).items(), key=lambda x: x[1], reverse=True)