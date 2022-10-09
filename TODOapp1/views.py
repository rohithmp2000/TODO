from asyncio import tasks
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Task

from .forms import Tasks

# Create your views here.
def index(request):
    data = Task.objects.all()
    return render(request, 'page1.html',{'data': data})
# def addtask(request):
#     return render(request, 'add.html')

class List(ListView):
    # specify the model for list view
    model = Task

def addtask(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Tasks(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/app1')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Tasks()
        context ={}

    context['form']= form
    return render(request, 'add.html', {'form': form})

def delete(request,id):
    items = Task.objects.get(id=id) 
    items.delete()
    return redirect('/app1') 

def complete(request,id):
    items = Task.objects.get(id=id) 
    items.is_complete=True
    items.save()
    return redirect('/app1') 

def completed(request):
    data = Task.objects.filter(is_complete=True)
    return render(request, 'complete.html',{'data': data})

def pending(request):
    data = Task.objects.filter(is_complete=False)
    return render(request, 'pending.html',{'data': data})