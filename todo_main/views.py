#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')## this is used to order the data by update this
    
    task_Done=Task.objects.filter(is_completed=True)
    
    context={
        'tasks':tasks,
        'task_Done': task_Done,
    }
    return render(request,'home.html',context)
   
    