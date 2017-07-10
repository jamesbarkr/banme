from django.shortcuts import render

import requests

from . import markovit

def main(request):
    """Main page for ban_me"""
    output = markovit.markovit_v2() # string output

    # context is info passed to the template using render
    context = {'output': output}

<<<<<<< HEAD
    return render(request, 'views/index.html', context)
=======
    return render(request, 'ban_me/main.html', context)
>>>>>>> 9aad4589baa90038a7312766dec3c4d62c63544d
