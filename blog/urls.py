#mysite/blog/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_cover/', views.bookCover, name='book_cover'),
    path('post/<slug:slug>/', views.post, name='post'),
]