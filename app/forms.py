from django import forms
from .models import Item, Info


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

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    class Meta:
        model = Info
        fields = ('name','image')