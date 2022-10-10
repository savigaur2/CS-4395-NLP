# CS-4395-NLP
Repo for CS-4395-NLP

## NLP Overview
This document provides an overview of NLP in my own words.

You can see the [document here](NLP_Overview.pdf)

## Assignment 1
This program performs text processing on a employee dataset to centralize the formatting of the first name, last name, middle inital, employee id, and phone number. The program uses regex for pattern matching and data validation. The program uses a person class to save the people in the dataset and saves them in a dictionary that is then saved in a pickle file. Finally, the employee list is displayed to the user.

You can see the [code here](Homework1/Homework1_sxg180113.py) and a [detailed document here](Homework1/Assignment1_Details.md)


## Assignment 2
This notebook demonstrates ome of the most useful functions of NLTK. The code also explores the nltk.Text API and shows the use of ```tokens```, ```concordance``` and ```count``` form the Tokens API. The code also makes use of ```work_tokenizer```, ```sent_tokenizer```, ```PorterStemmer``` and ```WordNetLemmatizer```

You can see the [code here](Homework2/Homework2_sxg180113.pdf) and a [detailed document here](Homework2/Assignment2_Details.md)

## Assignment 3
This program performs text processing on the ```anat19.txt``` file read in by command line arguments. This file is the text from one chapter of an anatomy textbook. The program calculates the lexical diversityof the tokens in the file, displays the lemmas, performs part-of-speech tagging, and displays the nouns present in the text. Next, the program presents the user with an interactive hangman guessing game based on the words from the text file. This game gives the user 5 points to start adn everytime they guess a letter correct, they gain one point, and everytime they guess a letter incorrect, they lose one point. The gane ends either when the user guess the word completely, the user has negative points, or if the user guesses a ```!```.

You can see the [code here](Homework3/Homework3_sxg180113.py) and a [detailed document here](Homework3/Assignment3_Details.md)

## Assignment 4
This notebook demonstrates the uses of ```WordNet``` and ```SentiWordNet``` in text analysis. Specifically, the notebook explores ```synsets``` in ```WordNet``` and ```senti_synsets``` in ```SentiWordNet``` along with part-of-speach tagging and word relations through hyper/hypo/mero/holo/anto-nyms.

You can see the [code here](Homework4/Homework4_sxg180113.pdf) and a [detailed document here](Homework4/Assignment4_Details.md)

## Assignment 5
This program consists of two parts: language model and language classifications. The language model uses ```bigrams``` and ```unigrams``` from ```nltk``` to creat unigram and bigram dictionaries based on the training data. This part of the program creates separate language models for English, French and Italian which will be used later during the classification phase. The language classifications read in the test file and calculate the probability of each line being either English, Frech or Italian using ```laplace smoothing``` by the following equation: $$ P = \frac{b + 1}{u + V} $$, where b is
the bigram count, u is the unigram count of the first word in the bigram, and v is the total vocabulary
size (add the lengths of the 3 unigram dictionaries). This phase also calculates the accuracy of the language models.

You can see the [code here](Homework5/ngrams.py) and a [detailed document here](Homework5/Assignment5_Details.md)

## Assignment 6
This program combines many useful and practical applications of NLP into one project. The program creates a ```web crawler``` using ```BeatifulSoup``` to scrape related urls from the MyAnimeList website. The program scrapes all of the text off the urls and cleans them using ```nltk```'s ```sentence tokenizer``` combined with stopwords and filtering for tabs and new lines. Then, the ```TFIDF``` is used to determine the most important words from all of the urls to be used in a knowledge base for a chatbot which will be developed in the future. You can see a [report document here](Homework6/Report.pdf)

You can see the [code here](Homework6/Homework6_sxg180113.py) and a [detailed document here](Homework6/Assignment6_Details.md)
