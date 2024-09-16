#-------------------------------------------------------------------------
# AUTHOR: Hoang Tu Huynh
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math
from collections import Counter

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.

stopWords = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'and', 'or', 'but', 'if', 'because', 'as', 'while', 'of', 'the', 'in', 'on', 'at', 'for'}

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.

stemming = {
    'loves': 'love',
    'dogs': 'dog',
    'cats': 'cat',
}

#Identifying the index terms.



def clean_document(doc):
    tokens = doc.lower().split()
    cleaned_tokens = []
    for token in tokens:
        if token not in stopWords:
            stemmed_token = stemming.get(token, token)  # Apply stemming if possible
            cleaned_tokens.append(stemmed_token)
    return cleaned_tokens

cleaned_documents = [clean_document(doc) for doc in documents]

terms = sorted(set(term for doc in cleaned_documents for term in doc))

def tf(term, doc):
    return doc.count(term) / len(doc)

def idf(term, docs):
    n_docs_with_term = sum(1 for doc in docs if term in doc)
    return math.log(len(docs) / (1 + n_docs_with_term))

#Building the document-term matrix by using the tf-idf weights.

docTermMatrix = []
for doc in cleaned_documents:
    term_weights = []
    for term in terms:
        tf_value = tf(term, doc)
        idf_value = idf(term, cleaned_documents)
        tf_idf = tf_value * idf_value
        term_weights.append(tf_idf)
    docTermMatrix.append(term_weights)

#Printing the document-term matrix.
print("Document-Term Matrix (TF-IDF Weights):")
print(f"Terms: {terms}")
for i, row in enumerate(docTermMatrix):
    print(f"Document {i+1}: {row}")