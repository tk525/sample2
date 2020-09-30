from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView # 追記
from django.contrib.auth.forms import UserCreationForm  # 追記
from django.urls import reverse_lazy # 追記
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
class IndexView(TemplateView):
    # template_name = "index.html"
    form_class = LoginForm
    template_name = "create.html"
    success_url = reverse_lazy("login")





class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"


# 追記
class UserCreateView(CreateView):
    form_class = LoginForm
    template_name = "create.html"
    success_url = reverse_lazy("login")