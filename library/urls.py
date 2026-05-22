from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/books/', views.book_list, name='book_list'),
    
]