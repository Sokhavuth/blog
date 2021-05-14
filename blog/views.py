#mysite/blog/views.py
from django.shortcuts import render


def index(request):
    from .controllers import _index
    kdict = _index.call()
    return render(request, 'base.html', context=kdict)


def bookCover(request):
    from .controllers import _bookCover
    kdict = _bookCover.call()
    return render(request, 'bookcover.html', context=kdict)


