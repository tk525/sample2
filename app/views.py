from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .filters import *
from .forms import *

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('')
    template_name = 'app/user_signup.html'


class ProfileView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        return render(self.request,'app/user_profile.html')



# info一覧画面
class InfoFilterView(FilterView):
    model = Info
    

class InfoCreateView(LoginRequiredMixin, CreateView):
    model = Info
    form_class = InfoForm
    success_url = reverse_lazy('')


class InfoDetailView(DetailView):
    model = Info


class InfoUpdateView(LoginRequiredMixin, UpdateView):
    model = Info
    form_class = InfoForm
    success_url = reverse_lazy('')


class InfoDeleteView(LoginRequiredMixin, DeleteView):
    model = Info
    success_url = reverse_lazy('')



class ItemFilterView(FilterView):
    model = Item
    filterset_class = ItemFilter
    queryset = Item.objects.all().order_by('-created_at')
    strict = False
    paginate_by = 10

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    #いいねボタンみたいなbuy
    def Buys(request, user_id, item_id):
        if request.method == 'POST':
            query = Buys.objects.filter(user_id=user_id, item_id=item_id)
            if query.count() == 0:
                buys_tbl = Buys()
                buys_tbl.user_id = user_id
                buys_tbl.item_id = item_id
                buys_tbl.save()
            else:
                query.delete()

            # response json
            # return JsonResponse({"status": "responded by views.py"})


class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')