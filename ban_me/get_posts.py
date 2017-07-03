import requests
from . import markovit
import time
import datetime

def get():
    # get data and return a status code (200 = good, 429 = bad)
    url = 'https://www.reddit.com/r/marchagainsttrump/top.json'
    headers = {'User-agent': 'u/eskimopies webapp ban_me, alpha testing using Django, requests'} # verbose user agent
                                                                                                 # allows more API requests
    r = requests.get(url, headers)
    if r.status_code == 200:
        print("Code good.")
    elif r.status_code == 429:
        print("Too many requests, attempting to resolve.",
            "(" + str(datetime.datetime.now().time()) + ")")
        while r.status_code != 200: # retries the request if a 429 status error is returned
            r = requests.get(url, headers)
            if r.status_code != 200:
                time.sleep(1) # allows 1 second between requests
    else:
        print("Unknown error, check stack trace.")

    # store API response in a var
    response_dict = r.json()

    # process results
    post_titles = []

    # turn the json data into a list of strings (titles)
    for post in response_dict['data']['children']:
        post_titles.append(post['data']['title'])

    return post_titles
