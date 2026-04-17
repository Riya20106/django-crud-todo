
from django.shortcuts import render 
from todos.models import task

def home(request):  
   tasks = task.objects.filter(is_completed= False).order_by('-updated_at')
   
   completedtask = task.objects.filter(is_completed=True)
   context = { 
      'tasks' :  tasks,
      'completedtask' : completedtask,
   }
   return render(request, 'home.html', context)
