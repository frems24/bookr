from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('book-search', views.book_search),
]
