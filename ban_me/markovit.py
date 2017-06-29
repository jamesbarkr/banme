"""The code for building a Markov chain output"""

import random
import re
from . import sample

# sampletext = sample.sample() # for offline testing

def markovit(textlist): # NOW REDUNDANT
    """
    A function which turns an input list (strings) into a Markov'd
    output
    """
    # the n part of the ngram
    order = 6 # increase/decrease this number to have the output make more/less sense, respectively
    # a dictionary to keep the ngrams in
    ngrams = {}
    # a function which iterates through the list of posts
    for text in textlist:
        i = 0
        while i < ((len(text) - order) - 1): # convoluted code to avoid out-of-range errors
            # sets the current gram equal to a spliced bit of text as
            # as long as the order
            gram = text[i:(i + order)]
            # if the gram isn't in the dictionary yet, make a key and
            # set an empty list as the value
            if gram not in ngrams.keys():
                ngrams[gram] = []
            # adds the letter following the gram to the list in the dict
            ngrams[gram].append(text[i + order])
            i += 1

    currentGram = textlist[random.randrange(len(textlist))][0:order] # picks a starting gram from a random title
    result = currentGram

    j = 0 # TODO find a way to make this prettier
    while j < 100: # <-- increase this number for longer string output
        j += 1
        if currentGram in ngrams: # fixed recurring KeyError
            possibilities = ngrams[currentGram] # the potential next letters
            nextletter = possibilities[random.randrange(len(possibilities))] # TODO: remove redundancy
            result += nextletter # appends the next letter to the result
            currentGram = result[(len(result) - order):len(result)] # makes a new currentGram from the appended result

    return result

def markovit_v2(titlelist):
    """The word-based version of the markov chain gen above"""
    return_len = 20
    word_freq = {}
    for title in titlelist:
        words = title.split() # splits string into words
        for word in words:
            if word not in word_freq.keys(): # if a list value does not exist in the
                word_freq[word] = []         # dict yet, create one
        i = 0
        while i < len(words): # super janky js-style loop TODO beautify this
            currentWord = words[i]
            print(currentWord)
            if i < (len(words) - 1):
                nextWord = words[i + 1]
                word_freq[currentWord].append(nextWord)
            i += 1

    return word_freq
