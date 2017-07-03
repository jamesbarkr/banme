import requests
from . import markovit
import time

def get():
    url = 'https://www.reddit.com/r/marchagainsttrump/top.json'
    headers = {'User-agent': 'u/eskimopies'}
    r = requests.get(url, headers)
    print("Status code: ", r.status_code)
    if r.status_code == 200:
        print("Code good.")
    else:
        print("Bad status.")

    # store API response in a var
    response_dict = r.json()

    # process results
    post_titles = []

    #attempt to get dict
    response = {}
    while bool(response) == False:
        try:
            response = response_dict['data']
        except KeyError:
            print('error')
        time.sleep(5)

    # turn the json data into a list of strings (titles)
    for post in response['children']:
        post_titles.append(post['data']['title'])

    # run the post data through markovit
    return markovit.markovit_v2(post_titles)
