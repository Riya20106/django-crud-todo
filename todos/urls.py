
from django.urls import path 
from .import views 
urlpatterns = [ 
    path('addtask/' , views.addtask,name='addtask'),
    path('markasdone/<int:pk>/',views.markasdone,name='markasdone'),
    path('markundone/<int:pk>/',views.markundone,name='markundone'), 
    path('delete_task/<int:pk>/',views.delete_task,name='delete'), 
    path('edit_task/<int:pk>/',views.edit_task,name='edit')
]