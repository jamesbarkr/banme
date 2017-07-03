"""The code for building a Markov chain output"""

import random
from .models import Post

def wordlistgen(titlelist):
    """Generates a a dictionary of words, each with a dictionary of potential following words"""
    word_freq = {}
    for title in titlelist:
        words = title.split() # splits string into words

        for word in words:
            if word not in word_freq.keys(): # if a list value does not exist in the
                word_freq[word] = []         # dict yet, create one

        for num in range(len(words)): # a for loop which populates the lists in the dictionary
            currentWord = words[num]
            if num < (len(words) - 1):
                nextWord = words[num + 1]
                word_freq[currentWord].append(nextWord)

    return word_freq

def markovit_v2():
    titlelist = []
    posts = Post.objects.all()
    for post in posts:
        titlelist.append(post.title)
    word_freq = wordlistgen(titlelist) #
    return_len = 10 # the length of the returned string

    startSource = titlelist[random.randrange(len(titlelist))]
    currentWord = startSource.split()[0] # selects a 'first word' from among the posts
    result = '' # initializes the result sentence

    for j in range(return_len):
        possibilities = word_freq[currentWord] # gets all possible next words
        if len(possibilities) != 0: # if there is at least one possibility, carry on.
            nextWord = possibilities[random.randrange(len(possibilities))]
        else: # this entire part of the loop should be REMOVED <-- TODO its for making sure its not broken
            possibilities = []
            for word in word_freq.keys():
                possibilities.append(word)
            nextWord = possibilities[random.randrange(len(word_freq.keys()))]
        result += ' ' + nextWord
        currentWord = nextWord

    return result
