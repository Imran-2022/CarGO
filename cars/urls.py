from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_post,name='add_post'),
    path('car_details/<int:id>',views.car_details,name='car_details'),
    path('edit/<int:id>',views.edit_post,name='edit_post'),
    path('delete/<int:id>',views.delete_post,name='delete_post')
]
