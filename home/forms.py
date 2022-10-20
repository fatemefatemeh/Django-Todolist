from django import forms
from .models import Todo
from django.forms import ModelForm


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
