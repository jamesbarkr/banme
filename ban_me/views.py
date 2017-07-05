from django.shortcuts import render

import requests

from . import markovit

def main(request):
    """Main page for ban_me"""
    output = markovit.markovit_v2() # string output

    # context is info passed to the template using render
    context = {'output': output}

    return render(request, 'views/index.html', context)
