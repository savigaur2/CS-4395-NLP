# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zqK1RZtyzY7MJkC_gMebV7M6t3VjTxd1
"""

from bs4 import BeautifulSoup
import urllib
from urllib import request
import os
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pickle

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def relevant_urls (soup):
    urls_list = []
    counter = 0
    for link in soup.find_all('a'):
        if counter > 15:
            break
        url = str(link.get('href'))
        if ('ad.' not in url) and (url != 'None') and (len(url) > 1):
            urls_list.append(url)
            counter += 1
    return urls_list

def scrape_pages (urls_list):
    for idx, url in enumerate(urls_list):
        html = request.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, features = 'html.parser')
        for script in soup(['script', 'style']):
            script.extract()
        text = soup.get_text()
        file_name = 'URL_' + str(idx)
        with open('UrlsText/' + file_name + '.txt', 'w') as f:
            f.write(text)

def clean_up_pages ():
    directory = 'UrlsText'

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        cleaned_file_path = file_path[:-4] + '_cleaned.txt'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as read_file:
                with open(cleaned_file_path, 'w') as write_file:
                    text = read_file.read()
                    text = text.replace('\t', ' ')
                    text = text.replace('\n', '')
                    sents = nltk.sent_tokenize(text)
                    for sent in sents:
                        write_file.write(sent)

# Source: https://github.com/kjmazidi/NLP/blob/master/Part_4-Documents/Explore%20ACL2020%20abstracts.ipynb
def preprocess (docs, stopwords):
    """
    Tokenize, remove stopwords and non-alpha tokens.
    param: docs - a list of raw text documents
    return: a list of processed tokens
    """
    wnl = WordNetLemmatizer()
    processed_docs = []
    for doc in docs:
        tokens = [wnl.lemmatize(t) for t in word_tokenize(doc.lower()) if t.isalpha()]
        tokens = [t for t in tokens if t not in stopwords]
        processed_docs.append(tokens)

    return processed_docs

def extract_important_terms ():
    docs_master = []
    count_vectorizer = CountVectorizer()
    directory = 'UrlsText'

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if 'cleaned' in file_path:
            with open(file_path, 'r') as f:
                # Source: https://github.com/kjmazidi/NLP/blob/master/Part_4-Documents/Explore%20ACL2020%20abstracts.ipynb
                docs = f.read().lower().splitlines()
                stopword_list = nltk.corpus.stopwords.words('english')
                preprocessed_docs = preprocess(docs, stopword_list)
                docs2 = [' '.join(doc) for doc in preprocessed_docs]
                for x in docs2:
                    docs_master.append(x)

    # TFIDF
    word_counts = count_vectorizer.fit_transform(docs_master)
    tfidf_transformer = TfidfTransformer(smooth_idf = True, use_idf = True)
    tfidf_transformer.fit(word_counts)

    # Extract idf values
    df_idf = pd.DataFrame(tfidf_transformer.idf_, index = count_vectorizer.get_feature_names(),columns = ["idf_weights"])
    results = df_idf.sort_values(by = 'idf_weights', ascending = False)
    display(results[:40])

# Knowledge Base
def create_knowledge_base () :
    kb = {'Who is the main villain in kimestsu no yaiba?': 'muzan',
        'What was the flame alchemists name in FMAB?': 'mustang',
        'What is daughter in Japanese?': 'musuko',
        'What did one for all call people with quirks?': 'mutant',
        'Arancars lived in hueco': 'mundo',
        'What was Johan Liebert being chsed for being?': 'murderer',
        'Who made the ending song of Joshiraku?': 'musicnippon',
        'What is difficult in Japanese?': 'muzukashii',
        'What is the anime about the guy who groes up as a secret soldier and joins a school with 5 mysterious girls?': 'novelgrisaia',
        'What is villager in Japanese?': 'murabito'}

    with open('kb.pickle', 'wb') as handle:
        pickle.dump(kb, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    url = 'https://myanimelist.net/'
    html = request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, features = 'html.parser')

    urls_list = relevant_urls(soup)
    scrape_pages(urls_list)
    clean_up_pages()
    extract_important_terms()
    create_knowledge_base()