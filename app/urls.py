from django.urls import path
from .views import *
from django.contrib import admin
# from django.urls import path, include 

# app_name = 'app'

urlpatterns = [
    # path('',  index_img, name='index_img'),
    
    #User
    path('user_create',  UserCreateView.as_view(), name='user_create'),


    #info
    path('',  InfoFilterView.as_view(), name=''),
    path('info_create/', InfoCreateView.as_view(), name='info_create'),
    path('info_detail/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
    path('info_update/<int:pk>/', InfoUpdateView.as_view(), name='info_update'),
    path('info_delete/<int:pk>/', InfoDeleteView.as_view(), name='info_delete'),


    #online/item
    path('index/',  ItemFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),

]
