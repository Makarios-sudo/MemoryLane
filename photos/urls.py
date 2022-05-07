
from django.urls import path
from . import views




urlpatterns = [

    
    path('memoryGallery', views.memoryGallery, name="memoryGallery"),

    #Crud operation for category
    path('addCategory/', views.addCategory, name="addCategory"),
    path('deleteCategory/<str:pk>/', views.deleteCategory, name="deleteCategory"),

    #Crud operation for Memory
    path('view/<str:pk>/', views.viewMemory, name="viewMemory"),
    path('add/<str:pk>/', views.addMemory, name="addMemory"),
    path('updateMemory/<str:pk>/', views.updateMemory, name="updateMemory"),
    path('deleteMemory/<str:pk>/', views.deleteMemory, name="deleteMemory"),

    

]
