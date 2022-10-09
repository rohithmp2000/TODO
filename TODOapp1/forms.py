from django import forms

from .models import Task

# class Tasks(forms.Form):
#     TaskName = forms.CharField(label='TaskName', max_length=100)

class Tasks(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Task
        fields = ('taskname',)