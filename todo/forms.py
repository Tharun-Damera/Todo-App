from django.forms import *
from django.utils import timezone
from .models import TodoModel

class TodoModelForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'info']

        widgets = {
            'title' : TextInput(attrs={'class': 'form-control mg shadow-lg', 
                                       'placeholder' : 'Title'}),
            'info' : Textarea(attrs={'class': 'form-control mg shadow-lg', 
                                     'placeholder' : 'Here goes the details of the todo...', 
                                     'rows' : '3'}),
        }

        