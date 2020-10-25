from django import forms
from django.forms import ModelForm

from .models import Todo

class TodoForm(forms.ModelForm):
    title=forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new text'}))

    class Meta:
        model = Todo
        fields = '__all__'



