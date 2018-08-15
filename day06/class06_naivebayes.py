# pip install nltk

import nltk
nltk.download('names')
from nltk.corpus import names
import random

names = ([(name, 'male') for name in names.words('male.txt')] +
  [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

## Define training and test set sizes
len(names)
train_size = 5000


## A simple feature
def g_features1(word):
  return {'last_letter': word[-1]}

## Msc:
def return_two():
  return 5, 10

x, y = return_two()

## Loop over names, return tuple of last letter and label
features = [(g_features1(n), g) for (n,g) in names]
train_set, test_set = features[:train_size], features[train_size:]
classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.classify(g_features1('Neo'))
classifier.classify(g_features1('Trinity'))
classifier.classify(g_features1('Max'))
classifier.classify(g_features1('Lucy'))
classifier.prob_classify(g_features1('Lucy')).prob("female")

## Check the overall accuracy with test set
print nltk.classify.accuracy(classifier, test_set)

## Lets see what is driving this
classifier.show_most_informative_features(5)


## Lets be smarter
## What all are we including now?
def g_features2(name):
  features = {}
  features["firstletter"] = name[0].lower()
  features["lastletter"] = name[-1].lower()
  for letter in 'abcdefghijklmnopqrstuvwxyz':
      features["count(%s)" % letter] = name.lower().count(letter)
      features["has(%s)" % letter] = (letter in name.lower())
  return features

features = [(g_features2(n), g) for (n,g) in names]
train_set, test_set = features[:train_size], features[train_size:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)


## Worse? Better? How can we refine?
# Lets look at the errors from first model and see if we can do better
errors = []
for (name, tag) in test_names:
  guess = classifier.classify(g_features2(name))
  if guess != tag:
    prob = classifier.prob_classify(g_features2(name)).prob(guess)
    errors.append((tag, guess, prob, name))


for (tag, guess, prob, name) in sorted(errors):
  print 'correct=%-10s guess=%-10s prob=%-10s name=%-10s' % (tag, guess, prob, name)




## What should we do here?
def g_features3(name):


features = [(g_features3(n), g) for (n,g) in names]
train_set, test_set = features[:train_size], features[train_size:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)





# Now lets look at some bigger documents
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')

## list of tuples
## ([words], label)
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

documents[0]

## Dictionary of words and number of instances
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
len(all_words)
word_features = [k for k in all_words.keys() if all_words[k] > 5]


for w in word_features:
  print all_words[w]

def document_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
  return features

print document_features(movie_reviews.words('pos/cv957_8737.txt'))

## Now we have tuple of ({features}, label)
features = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = features[1000:], features[:1000]
len(train_set)
len(test_set)
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(5)

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.