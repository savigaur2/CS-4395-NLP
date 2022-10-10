# Assignment 6 Details

## Program Description
This program combines many useful and practical applications of NLP into one project. The program creates a ```web crawler``` using ```BeatifulSoup``` to scrape related urls from the MyAnimeList website. The program scrapes all of the text off the urls and cleans them using ```nltk```'s ```sentence tokenizer``` combined with stopwords and filtering for tabs and new lines. Then, the ```TFIDF``` is used to determine the most important words from all of the urls to be used in a knowledge base for a chatbot which will be developed in the future. You can see a [report document here](Homework6/Report.pdf)

## How to run the proram
The program can be run using the following command: ```python3 Homework6_sxg180113.py```

## What I learned from this assignment
In this assignment I learned how to use ```BeautifulSoup``` to extract text data from external web URLS. I also learned how to extract important workds from a collection of documents using ```TFIDF``` scores.