import stopwordsiso as stopwords

# https://github.com/stopwords-iso/stopwords-iso
# stopwords_iso = stopwords.stopwords(langs="en")
with open("c://bronto1//data//stopwords//stopwords_iso.csv", "r") as file:
    stop_iso = [line.strip() for line in file]

# https://countwordsfree.com/stopwords
with open("c://bronto1//data//stopwords//stopwords_cwf.txt", "r", encoding="utf-8") as file:
    stop_cwf = [line.strip() for line in file]

# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# stopwords = stopwords.words('english')
with open("c://bronto1//data//stopwords//stopwords_nltk.csv", "r", encoding="utf-8") as file:
    stop_nltk = [line.strip() for line in file]

# http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/a11-smart-stop-list/english.stop
with open("c://bronto1//data//stopwords//stopwords_smart.csv", "r") as file:
    stop_smart = [line.strip() for line in file]