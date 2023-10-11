# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Artist
from listings.models import Title

def hello(request):
    bands = Band.objects.all()
    titles = Title.objects.all()
    artists = Artist.objects.all()
    return render(request, 'listings/hello.html')
    return render(request,
    'bands/hello.html',
    {'bands': bands})


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>contactez-nous</h1> <p>Nous restons a lécoute!</p>')

def listings(request):
    return HttpResponse('<h1>Liste</h1> <p>Voici les différentes listes!</p>')

