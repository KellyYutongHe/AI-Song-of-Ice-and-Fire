from collections import defaultdict, Counter
from numpy import cumsum, sum, searchsorted
from numpy.random import rand
from random import randint
import pickle
import random
import string
import urllib2


def predict(phrase):
    probs = sorted(word_dict[phrase].iteritems(), key=lambda (k,v): (v,k), reverse = True)
    target = rand()*sum(probs.values())
    index = searchsorted(cumsum(probs.values()), target)[0]
    return probs[probs.keys()[index]]

def generate(start, n):
    result = start
    for i in range(n):
        new = predict(tuple(start.split(" ")))
        result += new
        start = start[1:] + new
    return result

def test(length):
    return ''.join(random.sample(string.hexdigits, int(length)))

def main():
    word_dict = {}
    word_dict = pickle.load(urllib2.urlopen("https://s3.us-east-2.amazonaws.com/modelsuperbig/grams.pickle"))

    print word_dict.keys()[1]
    print generate("I", 2)

if __name__ == "__main__":
    main()
