from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()


class UserCreateForm(UserCreationForm, forms.Form):

    user_or_owner = forms.IntegerField(initial=1)

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email','user_or_owner')
        else:
            fields = ('email','user_or_owner')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user_or_owner'].widget = forms.HiddenInput()

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','age','sex','memo','description', 'photo',)
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'for example：AirLight-20'}),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }


class InfoForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = ('name','season','info')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'for example：AirLight-20'}),
                    'season': forms.RadioSelect(),
                    'info': forms.Textarea(),
                  }
