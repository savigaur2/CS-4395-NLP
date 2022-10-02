# Assignment 5 Details

## Program Description
This program consists of two parts: language model and language classifications. The language model uses ```bigrams``` and ```unigrams``` from ```nltk``` to creat unigram and bigram dictionaries based on the training data. This part of the program creates separate language models for English, French and Italian which will be used later during the classification phase. The language classifications read in the test file and calculate the probability of each line being either English, Frech or Italian using ```laplace smoothing``` by the following equation: $$ P = \frac{b + 1}{u + V} $$, where b is
the bigram count, u is the unigram count of the first word in the bigram, and v is the total vocabulary
size (add the lengths of the 3 unigram dictionaries). This phase also calculates the accuracy of the language models.

## How to run the program
The program cam be run by executing ```python3 ngrams.py```. An important thing to note is that the program reads the pickled dictionaries from the path to the google drive file, so make sure to save the dictionaires to the same lcoation as the path in the code or change the path to reflect the destination of the files.

## What I learned from this assignment
In this assignment, I learned how to use to create ```ngrams``` using ```nltk```, specifically ```unigrams``` and ```bigrams``` which can be used in language models. Also, I learned how to make language classificatons using ```laplace smoothing``` for calculating probabilities.