from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_book, name="search_book"),
    path('search/<int:id>/', views.book_info, name="book_info"),
    path('search/<int:id>/emanet/', views.book_emanet, name="book_emanet"),
    path('search/<int:id>/teslim/', views.book_teslim, name="book_teslim"),
]