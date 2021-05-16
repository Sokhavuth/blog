#mysite/blog/views.py
from django.shortcuts import render


def index(request):
    from .controllers import _index
    kdict = _index.call()
    return render(request, 'index.html', context=kdict)


def post(request, slug):
    from .controllers import _post
    kdict = _post.call(slug)
    return render(request, 'post.html', context=kdict)
    

def bookCover(request):
    from .controllers import _bookCover
    kdict = _bookCover.call()
    return render(request, 'bookcover.html', context=kdict)
