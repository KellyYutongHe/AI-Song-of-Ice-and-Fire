import os
import sys
import string
import re
import pickle
from collections import defaultdict

data_dir = "../"
files = [data_dir + i for i in os.listdir(data_dir) if "txt" in i]

def sep_punc(files, outputname):
    for filename in files:
        with open(filename, "r") as f, open(outputname, "a") as o:
            for line in f:
                for c in line:
                    if c in string.punctuation:
                        o.write(" "+c+" ")
                    else:
                        o.write(c)

def gram2seq(n, words):
    word_dict = {}
    for w in range(len(words)-n):
        if w%10000 == 0:
            print words[w]
        for i in range(1,n+1):
            gram = tuple([words[w+k] for k in range(i)])
            if not gram in word_dict:
                word_dict[gram] = {}
            word = str(words[w+i])
            if not word in word_dict[gram]:
                word_dict[gram][str(words[w+i])] = 1
            else:
                word_dict[gram][str(words[w+i])] += 1
    return word_dict

def main():
    fullbook = data_dir + "got.txt"
    grampickle = "grams.pickle"
    # sep_punc(files, fullbook)
    words = []
    with open(fullbook, "r") as f:
        for line in f:
            for i in line.split(" "):
                if not i == "":
                    words.append(i)

    word_dict = gram2seq(5, words)
    with open(grampickle, "wb") as g:
        pickle.dump(word_dict, g)

if __name__ == "__main__":
    main()
