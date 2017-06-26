"""The code for building a Markov chain output"""

order = 5
ngrams = {}

def markovit(text):
    """
    A function which turns an input list (strings) into a Markov'd
    output
    """
    output = ''
    for item in text:
        output += ' ' + item
    return output # ( all of the above is placeholder code)

# not sure if project should parse text all at once or iterate through
# each post
