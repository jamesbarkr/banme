"""URL patterns for ban_me"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # main page
    url(r'^$', views.main, name='main'),
]
