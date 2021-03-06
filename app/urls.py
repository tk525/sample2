from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from .views import *

# app_name = 'app'


urlpatterns = [
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

    path('buys/', ItemFilterView.Buys, name='buys'),


    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),


    path('bought/<int:pk>/', UserBoughtView.as_view(), name='bought'),
    path('bought_cancel/', UserBoughtCancelView.as_view(), name='bought_cancel'),
    path('bought_decide/', UserBoughtDecideView.as_view(), name='bought_decide'),


    path('shipment/', ShipmentView.as_view(), name='shipment'),
    path('shipment_delete/<int:pk>/', ShipmentDeleteView.as_view(), name='shipment_delete'),

]
