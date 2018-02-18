from collections import defaultdict, Counter
from numpy import cumsum, sum, searchsorted
from numpy.random import rand
from random import randint
import pickle
import random
import string
import urllib2
import operator

def predict(phrase, word_dict):
    result = ""
    probs = sorted(word_dict[phrase].items(), key=operator.itemgetter(1), reverse = True)
    print probs
    target = rand()*sum([i[1] for i in probs])
    try:
        index = list(searchsorted(cumsum([i[1] for i in probs]), target))[0]
    except:
        index = searchsorted(cumsum([i[1] for i in probs]), target)
    if probs[index][0] == "'" or probs[index][0] == "The":
        result = predict(phrase, word_dict)
    else:
        result = probs[index][0]
    return result

def generate(start, n, word_dict):
    result = start
    for i in range(n):
        print start
        new = predict(tuple(start.split(" ")[-2:]),word_dict)
        print new
        result += " "
        result += new
        start = result
    return result

def test(length):
    return ''.join(random.sample(string.hexdigits, int(length)))

def main():
    word_dict = {}
#    word_dict = pickle.load(urllib2.urlopen("https://s3.us-east-2.amazonaws.com/modelsuperbig/grams.pickle"))
    with open("../grams.pickle", "rb") as f:
        word_dict = pickle.load(f)
    print word_dict.keys()[1]
    print generate("Storm", 150, word_dict)

if __name__ == "__main__":
    main()
