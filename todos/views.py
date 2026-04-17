from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse 
from .models import task 
# Create your views here.
def addtask(request): 
    newtask = request.POST['task']
    task.objects.create(task = newtask)
    return redirect('home')
 
def markasdone(request,pk):  
 c_task = get_object_or_404(task,pk=pk)
 c_task.is_completed =True
 c_task.save() 
 return redirect('home')

def markundone(request,pk):
 untask = get_object_or_404(task,pk=pk) 
 untask.is_completed = False 
 untask.save() 
 return redirect('home')  

def delete_task(request,pk): 
  dl_task = get_object_or_404(task,pk=pk)
  dl_task.delete() 
  return redirect('home')
   
def edit_task(request,pk): 
   gettask = get_object_or_404(task,pk=pk)
   
   if request.method =='POST': 
     new_task = request.POST['task']
     gettask.task = new_task 
     gettask.save()
     return redirect('home')
   else : 
     context ={ 
     'gettask' : gettask , 
     } 
     return render(request,'edit_task.html', context) 
   