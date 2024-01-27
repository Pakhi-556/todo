from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask,name='addTask'),
    path('markDone/<int:pk>',views.markDone,name='markDone'),
    path('markUnDone/<int:pk>',views.markUnDone,name='markUnDone'),

    ## edit feature
    path('editTask/<int:pk>/',views.editTask,name='editTask'),

    ## edit feature
    path('delTask/<int:pk>/',views.delTask,name='delTask'),



]

