from re import template
from django.urls import path,include
from .views import List, delete
from TODOapp1 import views

urlpatterns =[
    path('', views.index, name ='index'),
    path('addtask/', views.addtask, name ='addtask'),
    path('tasklist/', List.as_view(template_name = 'tasklist.html')),
    path('delete/<int:id>',views.delete,name='delete'),
    path('complete/<int:id>',views.complete,name='complete'),
    path('competed/', views.completed, name ='completed'),
    path('pending/', views.pending, name ='pending'),

]