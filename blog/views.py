#mysite/blog/views.py
from django.shortcuts import render
from .models import Post

def index(request):
    from .controllers import _index
    kdict = _index.call()
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    posts = [post for post in queryset]
    kdict['posts'] = posts
    return render(request, 'index.html', context=kdict)


def bookCover(request):
    from .controllers import _bookCover
    kdict = _bookCover.call()
    return render(request, 'bookcover.html', context=kdict)

