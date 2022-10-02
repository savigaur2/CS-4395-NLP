"""Ngrams.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1azy_PYF5wjIyDT8gGcDdZqydyOOGYnKG
"""

# How to read files from Google Drive: https://colab.research.google.com/notebooks/io.ipynb#scrollTo=RWSJpsyKqHjH
from google.colab import drive
drive.mount('/content/drive')
from nltk import word_tokenize
from nltk.util import ngrams
import nltk
nltk.download('punkt')
import pickle

#############
# Program 1 #
#############

def unigram_bigram(filename):
  with open(filename, 'r') as f:
    raw_text = f.read()

  tokens = word_tokenize(raw_text)
  bigrams = list(ngrams(tokens, 2))
  unigrams = list(ngrams(tokens, 1))
  bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}
  unigram_dict = {t:unigrams.count(t) for t in set(unigrams)}

  return unigram_dict, bigram_dict

english = '/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/ngram_files/LangId.train.English'
french = '/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/ngram_files/LangId.train.French'
italian = '/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/ngram_files/LangId.train.Italian'

english_unigram, english_bigram = unigram_bigram(english)
french_unigram, french_bigram = unigram_bigram(french)
italian_unigram, italian_bigram = unigram_bigram(italian)

with open('/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/pickle_files/english_unigram.pickle', 'wb') as handle:
    pickle.dump(english_unigram, handle)
with open('/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/pickle_files/english_bigram.pickle', 'wb') as handle:
    pickle.dump(english_bigram, handle)
with open('/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/pickle_files/french_unigram.pickle', 'wb') as handle:
    pickle.dump(french_unigram, handle)
with open('/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/pickle_files/french_bigram.pickle', 'wb') as handle:
    pickle.dump(french_bigram, handle)
with open('/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/pickle_files/italian_unigram.pickle', 'wb') as handle:
    pickle.dump(italian_unigram, handle)
with open('/content/drive/My Drive/Schoolwork/CS 4395/Ngrams/pickle_files/italian_bigram.pickle', 'wb') as handle:
    pickle.dump(italian_bigram, handle)

#############
# Program 2 #
#############

eng_uni_dict = pickle.load(open('/content/drive/MyDrive/Ngrams/pickle_files/english_unigram.pickle', 'rb'))
eng_bi_dict = pickle.load(open('/content/drive/MyDrive/Ngrams/pickle_files/english_bigram.pickle', 'rb'))
fr_uni_dict = pickle.load(open('/content/drive/MyDrive/Ngrams/pickle_files/french_unigram.pickle', 'rb'))
fr_bi_dict = pickle.load(open('/content/drive/MyDrive/Ngrams/pickle_files/french_bigram.pickle', 'rb'))
ital_uni_dict = pickle.load(open('/content/drive/MyDrive/Ngrams/pickle_files/italian_unigram.pickle', 'rb'))
ital_bi_dict = pickle.load(open('/content/drive/MyDrive/Ngrams/pickle_files/italian_bigram.pickle', 'rb'))

# p = (b + 1) / (u + v)
def compute_prob (text, unigram_dict, bigram_dict, V):
    p_laplace = 1

    unigrams_test = word_tokenize(text)
    bigrams_test = list(ngrams(unigrams_test, 2))

    for bigram in bigrams_test:
        b = bigram_dict[bigram] if bigram in bigram_dict else 0
        u = unigram_dict[(bigram[0], )] if (bigram[0], ) in unigram_dict else 0

        p_laplace = p_laplace * ((b + 1) / (u + V))
    
    # print("probability with laplace smoothing is %.5f" % p_laplace)
    return p_laplace

V = len(eng_uni_dict) + len(fr_uni_dict) + len(ital_uni_dict) 
classifications = {}

with open('/content/drive/MyDrive/Ngrams/ngram_files/LangId.test', 'rb') as handle:
    lines = handle.readlines()
    line_num = 1
    for line in lines:
        probs = {}
        
        line = line.decode('utf-8')
        p_eng = compute_prob(text = line, unigram_dict = eng_uni_dict, bigram_dict = eng_bi_dict, V = V)
        p_fr = compute_prob(text = line, unigram_dict = fr_uni_dict, bigram_dict = fr_bi_dict, V = V)
        p_ital = compute_prob(text = line, unigram_dict = ital_uni_dict, bigram_dict = ital_bi_dict, V = V)

        probs['English'] = p_eng
        probs['French'] = p_fr
        probs['Italian'] = p_ital

        classifications[line_num] = max(probs, key = probs.get)

        line_num += 1

with open('/content/drive/MyDrive/Ngrams/ngram_files/classifications.txt', 'w') as f:
    for key, value in classifications.items():
        f.write('%s %s\n' % (key, value))

correct_classifications = {}
with open('/content/drive/MyDrive/Ngrams/ngram_files/LangId.sol', 'r') as f:
    for line in f.readlines():
        line_num, lang = line.split()
        correct_classifications[line_num] = lang

num_correct = 0
incorrect_classified = []
for key, value in classifications.items():
    if classifications[key] == correct_classifications[str(key)]:
        num_correct += 1
    else:
        incorrect_classified.append(key)

accuracy = (num_correct / len(classifications)) * 100
print('Accuracy: ', accuracy)
print('Incorrectly classified: ', incorrect_classified)