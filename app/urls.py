from django.urls import path
# from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, InfoFilterView
from .views import *
from django.contrib import admin
# from django.urls import path, include 


urlpatterns = [
    path('',  index_img, name='index_img'),
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

    # info一覧画面
    path('',  InfoFilterView.as_view(), name='info_index'),
]
