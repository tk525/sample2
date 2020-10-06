from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from .views import *

# app_name = 'app'


urlpatterns = [
    # path('',  index_img, name='index_img'),
    path('',  InfoFilterView.as_view(), name=''),

    path('info_create/', InfoCreateView.as_view(), name='info_create'),
    path('info_detail/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
    path('info_update/<int:pk>/', InfoUpdateView.as_view(), name='info_update'),
    path('info_delete/<int:pk>/', InfoDeleteView.as_view(), name='info_delete'),


    path('index/',  ItemFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),

    path('buy/<int:user_id>/<int:item_id>', ItemFilterView.Buys, name='buy'),


    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
