from .models import *
from django.forms import ModelForm, TextInput


class Introduce(ModelForm):
    class Meta:
        model = Team
        exclude = [""]
        # fields = ["name", "slogan"]
        widgets = {
            # "id": ,
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название команды'
            }),
            "slogan": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш девиз'
            })
        }
