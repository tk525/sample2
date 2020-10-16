from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import *
from .filters import *
from .forms import *

User = get_user_model()



class UserBoughtDecideView(LoginRequiredMixin, DeleteView):

    template = loader.get_template('templates/app/user_bought.html')

    def database_save(request):

        model = Shipments
        shipments = Shipments()

        users_list_onece=request

        for i in range(1) :
            shipments.mail = users_list_onece['address']
            shipments.product_name = users_list_onece['name']
            shipments.price = users_list_onece['age']
            shipments.sex = users_list_onece['sex']
            shipments.save()

        return


    def pre_dbsave(request):

        users_list=request

        for i in range(len(users_list['buys'])):
            ulb=users_list['buys'][i]
            ulb['address']=users_list['address']

            UserBoughtDecideView.database_save(ulb)

        return


    def get(self, *args, **kwargs):

        model = User
        users_list = {}

        if self.request.GET.getlist('user_address', None):
            users_list['address']=self.request.GET.getlist('user_address', None)[0] #a@gmail.com

        users = User.objects.get(id=self.request.user.id) #a@gmail.com
        user_buys_queryset = users.buys.all() #<QuerySet [<Item: 1>, <Item: 2>]>
        users_list['buys']=list(user_buys_queryset.values()) 

        UserBoughtDecideView.pre_dbsave(users_list)

        users.buys.clear()

        return redirect('index')



class UserBoughtCancelView(LoginRequiredMixin, DeleteView):
    model = User
    template = loader.get_template('templates/app/user_bought.html')


    def get(self, *args, **kwargs):

        users = User.objects.get(id=self.request.user.id) #a@gmail.com
        user_buys_queryset = users.buys.all() #<QuerySet [<Item: 1>, <Item: 2>]>
        user_buys=list(user_buys_queryset.values()) #{'id': 1, 'name': '1', 'age': 1, 'sex': 1, 'memo': '1', 'created_at': datetime.datetime(2020, 10, 12, 10, 16, 13, 443189, tzinfo=<UTC>), 'description': '1', 'photo': 'documents/pexels-melvin-buezo-2529148_lsypz0n.jpg', 'uploaded_at': datetime.datetime(2020, 10, 12, 10, 16, 13, 444163, tzinfo=<UTC>)}, {'id': 2, 'name': '2', 'age': 2, 'sex': 1, 'memo': '2', 'created_at': datetime.datetime(2020, 10, 12, 10, 37, 48, 983327, tzinfo=<UTC>), 'description': '2', 'photo': 'documents/pexels-la-miko-3616764_0qKhRNP.jpg', 'uploaded_at': datetime.datetime(2020, 10, 12, 10, 37, 48, 984092, tzinfo=<UTC>)}]

        if self.request.GET.get('user_buy', None):
            str_value = self.request.GET.get('title', None) #2

        if self.request.GET.getlist('user_buy', None):
            str_value=self.request.GET.getlist('user_buy', None)[0]
            
        int_value = int(str_value)-1 #1
        users.buys.remove(user_buys_queryset[int_value])

        return redirect('index')



class UserBoughtView(LoginRequiredMixin, FilterView):
    model = User

    def get(self, *args, **kwargs):
        template = loader.get_template('templates/app/user_bought.html')
        context = super().get(*args, **kwargs)

        users = User.objects.get(id=self.request.user.id) #a@gmail.com
        user_buys_queryset = users.buys.all() #<QuerySet [<Item: 1>, <Item: 2>]>
        user_buys=list(user_buys_queryset.values()) #{'id': 1, 'name': '1', 'age': 1, 'sex': 1, 'memo': '1', 'created_at': datetime.datetime(2020, 10, 12, 10, 16, 13, 443189, tzinfo=<UTC>), 'description': '1', 'photo': 'documents/pexels-melvin-buezo-2529148_lsypz0n.jpg', 'uploaded_at': datetime.datetime(2020, 10, 12, 10, 16, 13, 444163, tzinfo=<UTC>)}, {'id': 2, 'name': '2', 'age': 2, 'sex': 1, 'memo': '2', 'created_at': datetime.datetime(2020, 10, 12, 10, 37, 48, 983327, tzinfo=<UTC>), 'description': '2', 'photo': 'documents/pexels-la-miko-3616764_0qKhRNP.jpg', 'uploaded_at': datetime.datetime(2020, 10, 12, 10, 37, 48, 984092, tzinfo=<UTC>)}]
        
        total_price=0
        for i in range(len(user_buys)):
            total_price = list(user_buys)[i]['age']+total_price 

        context={
            'user_buys':user_buys,
            'total_price':total_price,
            'user_address':users,
        }

        return HttpResponse(template.render(context))



class UserSignUpView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('')
    template_name = 'templates/app/user_signup.html'


class UserProfileView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        return render(self.request,'templates/app/user_profile.html')



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
    def Buys(request):
        item = get_object_or_404(Item, id=request.POST.get('item_id'))
        boought = False
        if item.buys.filter(id=request.user.id).exists():
            item.buys.remove(request.user)
            bought = False
        else:    
            item.buys.add(request.user)
            bought = True

        context={
            'item': item,
            'bought': bought,
        }    
        if request.is_ajax():
            html = render_to_string('templates/app/item_filter.html', context, request=request )
            return JsonResponse({'form': html})



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