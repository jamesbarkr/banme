import requests
from . import markovit
import time
import json

def get():
    # get data and return a status code (200 = good, 429 = bad)
    url = 'https://www.reddit.com/r/marchagainsttrump/top.json'
    headers = {'User-agent': 'u/eskimopies webapp ban_me, alpha testing using Django, requests'}
    r = requests.get(url, headers)
    if r.status_code == 200:
        print("Code good.")
    else:
        print("Too many requests, trying again in 1 minute")
        while r.status_code != 200:
            r = requests.get(url, headers)
            if r.status_code != 200:
                time.sleep(60)

    # store API response in a var
    response_dict = json.loads(r.text)
    print(response_dict)

    # process results
    post_titles = []

    response = response_dict['data']

    # turn the json data into a list of strings (titles)
    for post in response['children']:
        post_titles.append(post['data']['title'])

    # run the post data through markovit
    output = markovit.markovit_v2(post_titles)
