#mysite/blog/views.py
from django.shortcuts import render

context = {
    'siteTitle': 'កម្មវិធី Blog',
    'message': 'ស្វាគមន៍​មក​កាន់​កម្មវិធី​ Blog'
}

def index(request):
    return render(request, 'base.html', context=context)
