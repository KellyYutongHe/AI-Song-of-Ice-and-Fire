from collections import defaultdict, Counter
from numpy import cumsum, sum, searchsorted
from numpy.random import rand
from random import randint
import pickle

def predict(phrase):
    probs = sorted(word_dict[phrase].iteritems(), key=lambda (k,v): (v,k), reverse = True)
    target = rand()*sum(probs.values())
    index = searchsorted(cumsum(probs.values()), target)[0]
    return probs[probs.keys()[index]]

# Generates n characters from start.
def generate(self, start, n):
    result = start

    # Foreach in n
    for i in range(n):
        # Get the next letter
        new = self.predict(start)

        # Add that letter to our output
        result += new

        # Our next start should be the new, minus the first letter of the old. So "abc" -> "abcd" -> "bcd"
        start = start[1:] + new
    return result

def main():
    word_dict = {}
    with open("grams.pickle", "rb") as f:
        word_dict = pickle.load(f)

    print word_dict.keys()[1]
    print predict(("Young", ))

if __name__ == "__main__":
    main()
