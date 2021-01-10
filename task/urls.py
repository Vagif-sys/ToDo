from django.urls import path
from .import views


urlpatterns = [
    
     path('',views.index, name='list'),
     path('update_task/<int:id>/',views.updateTask, name='update_task'),
     path('delete/<int:id>/',views.deleteTask, name='delete_task')
]