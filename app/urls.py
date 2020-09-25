from django.urls import path
from .views import *
from django.contrib import admin
# from django.urls import path, include 


urlpatterns = [
    # path('',  index_img, name='index_img'),
    path('',  InfoFilterView.as_view(), name=''),
    path('info_create/', InfoCreateView.as_view(), name='info_create'),
    path('info_detail/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
    path('info_update/<int:pk>/', InfoUpdateView.as_view(), name='info_update'),
    path('info_delete/<int:pk>/', InfoDeleteView.as_view(), name='info_delete'),


    # 一覧画面
    path('index/',  ItemFilterView.as_view(), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', ItemCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),

]
