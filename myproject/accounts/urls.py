from django.urls import path
from .views import *

urlpatterns = [
    # path('', index),
    path('accounts/', IndexView.as_view(), name="accounts"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', MyLogoutView.as_view(), name="logout"),
    # path('create/', UserCreateView.as_view(),name="create"), # 追記
]