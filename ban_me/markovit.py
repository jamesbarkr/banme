"""The code for building a Markov chain output"""

# the n part of the ngram
order = 5
# a dictionary to keep the ngrams in
ngrams = {}

text = ["Tape Released of Trump Saying He Spies on Naked Girls Back Stage, “Because I'm The Owner of The Pageant”",
"TrumpCare",
"Lady Liberty will end Trump",
"The New York Times used a full page in this week's paper to print all of Donald Trump's lies",
"The Missing Part",
"Only I can fix it",
"Bob Casey tweets explitly the atrocities of the latest GOP healthcare bill",
"It really is a disaster",
"Trump Blames the Biggest Mistake of His Presidency on Obama",
"MRW when they say the Senate will pass the Republicare bill",
"Over 50? Trumpcare will raise your premiums $4,500.",
"Scum.",
"Mitch McConnell Refused to Meet With Group That Funded His Polio Recovery",
"Trump Just Bragged About Himself On Twitter--And Twitter Wasn't Having It",
"Zombie Trump Street Art, London U.K.",
"Remember Those 1,100 Jobs Trump Saved in Indiana? They’re Gone",
"New York Times used a full page to print Trump's lies since taking office",
"Today the Word Of The Day on my Dictionary App was 'Doublethink' and one of the example sentences reminded me of the current political environment in the US",
"If only there had been some prior indications...",
"Trump supporters cannot handle anonymity.",
"Do March for Life Protesters Remember the Time Trump Joked About Having Wanted to Abort One of His Children?",
"President Stephen Colbert in 2020?",
"$25B Mexican border wall. After Americans lose everything during trump presidency, the wall will actually keep US citizens out of Mexico.",
"Vladimir Putin: climate change is real - but it's good",
"proud daddy putin holding lil daddy trump"]


def markovit(textlist):
    """
    A function which turns an input list (strings) into a Markov'd
    output
    """
    # a function which iterates through the list of posts
    for text in textlist:
        i = 0
        print(text)
        while i < (len(text) - order + 1):
            # sets the current gram equal to a spliced bit of text as
            # as long as the order
            gram = text[i:(i + order)]
            # if the gram isn't in the dictionary yet, make a key and
            # set an empty list as the value
            if gram not in ngrams.keys():
                ngrams[gram] = []
            # adds the letter following the gram to the list in the dict
            # ngrams[gram].append(text[(i + order)]) # <-- out of range?
            i += 1
    return ngrams

# not sure if project should parse text all at once or iterate through
# each post

print(markovit(text))
