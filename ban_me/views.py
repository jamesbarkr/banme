from django.shortcuts import render
import requests

# Create your views here.

def main(request):
    """Main page for ban_me"""
    # get data and return a status code (200 = good, 429 = bad)
    url = 'https://www.reddit.com/r/marchagainsttrump/top.json'
    r = requests.get(url)
    print("Status code: ", r.status_code)

    # store API response in a var
    response_dict = r.json()

    # process results
    post_titles = []

    # turn the json data into a list of strings (titles)
    for post in response_dict['data']['children']:
        post_titles.append(post['data']['title'])

    # context is info passed to the template using render
    context = {'titles': post_titles}

    return render(request, 'ban_me/main.html', context)
