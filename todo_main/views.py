#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')## this is used to order the data by update this
    context={
        'tasks':tasks,
    }
    return render(request,'home.html',context)