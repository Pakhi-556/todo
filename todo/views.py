from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')## this is used to redirect to the same page


def markDone(request,pk):
       task=get_object_or_404(Task,pk=pk)
       task.is_completed= True
       task.save()
       return redirect('home')

def markUnDone(request,pk):
       task=get_object_or_404(Task,pk=pk)
       task.is_completed=False## edit the object 
       task.save()## save the object
       return redirect('home')

## function for edit task

def editTask(request,pk):
    get_task= get_object_or_404(Task,pk=pk)

    if(request.method=='POST'):
          newtask=request.POST['task'] ##here task is name of tag  
          get_task.task=newtask
          get_task.save()
          return redirect('home')
    else:
        context={
              'get_task': get_task,  
        }
              
        return render(request,'editTask.html',context)
    
def delTask(request,pk):
    task= get_object_or_404(Task,pk=pk)   
    task.delete()
    return redirect('home')