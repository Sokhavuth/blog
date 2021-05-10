#mysite/blog/views.py
from django.shortcuts import render


def index(request):
    from .controllers import _index
    kdict = _index.call()
    return render(request, 'base.html', context=kdict)
