import sys
from nltk import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

def raw_text_processing (raw):
    # tokenize the lower-case raw text, reduce the tokens to only those that are alpha, not in
    # the NLTK stopword list, and have length > 5
    tokens5 = [t.lower() for t in word_tokenize(raw)
              if ((t.isalpha()) and (t not in stopwords.words('english'))
                and (len(t) > 5))]

    # lexical diversity
    print('Lexcial diversity: ', len(set(tokens5)) / len(tokens5))

    # lemmatize the tokens and use set() to make a list of unique lemmas
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens5]
    lemmas_unique = list(set(lemmas))

    # POS tagging
    tags = pos_tag(lemmas_unique)
    print('First 20 POS Tags: ', tags[0:20])

    # create a list of only those lemmas that are nouns
    lemmas_nouns = [noun for noun, tag in tags if tag == 'NN']

    # print the number of tokens (from step a) and the number of nouns (step d)
    print('Number of tokens: ', len(tokens5))
    print('Number of nounds: ', len(lemmas_nouns))

    return tokens5, lemmas_nouns

def guessing_game (common_50):
    print('------------------------------------')
    print('Lets play a guessing game!')

    # give the user 5 points to start
    user_points = 5
    guess_condition = False

    # randomly choose one of the 50 words
    rand = random.choice(common_50)
    print('REMOVE BEFORE SUBMITTING -- word: ', rand)

    output = []
    # output to console an underscore space for each letter in the word
    for letter in rand:
        output.append('_ ')
    print(output)

    while user_points >= 0:
        # ask the user for a letter
        user_letter = input('Guess a letter: ')

        if user_letter == '!':
            return

        # if the letter is in the word print Right!, fill in all matching letter and add 1 to the score
        if user_letter != '':
            if user_letter in rand:
                user_points += 1
                print('Right! Score is ', user_points)
                for idx, letter in enumerate(rand):
                    # print(letter, user_letter)
                    if letter == user_letter:
                        print(idx, letter)
                        output[idx] = letter
            else:
                user_points -= 1
                print('Sorry, guess again. Score is, ', user_points)
        else:
            print('Invalid guess')
        print(output)

        if output.count('_ ') == 0:
            print('You solved it!')
            print(output)
            print('------------------------------------')
            return user_points

    return user_points

if __name__ == '__main__':
    # Path error hanlding
    if len(sys.argv) == 1:
        print('Error, no path specified')
        exit(0)
    else:
        path = sys.argv[1]
        # Read in as raw text
        raw = open(path).read()

        # Calculate lexical diversity

        # Raw text processing
        tokens, nouns = raw_text_processing(raw)

        # Dictionary of {non: count of non in tokens}
        noun_counts_dict = {}
        for n in nouns:
            n_count_tokens = tokens.count(n)
            noun_counts_dict[n] = n_count_tokens

        # sort the dict by count and print the 50 most common workds and their counts
        common_50 = [word for word in sorted(noun_counts_dict, key = noun_counts_dict.get, reverse = True)[0:50]]
        print('50 most common words: ', common_50)
        print()

        # guessing game
        user_points = guessing_game(common_50)
        if user_points < 0:
            print('YOU LOST!')
