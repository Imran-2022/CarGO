# from django.contrib import admin
# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path('add/',views.add_post,name='add_post'),
#     path('car_details/<int:id>',views.car_details,name='car_details'),
#     path('profile/',views.order_history,name='profile'),
#     path('add_comment/<int:id>/', views.add_comment, name='add_comment'),
#     path('buy_now/',views.buy_now,name='buy_now'),
#     path('edit/<int:id>',views.edit_post,name='edit_post'),
#     path('delete/<int:id>',views.delete_post,name='delete_post')
# ]


# convert into class based view

from django.urls import path
from .views import AddPostView, EditPostView, CarDetailsView, DeletePostView, BuyNowView, AddCommentView,order_history

urlpatterns = [
    path('add/', AddPostView.as_view(), name='add_post'),
    path('edit/<int:id>/', EditPostView.as_view(), name='edit_post'),
    path('car_details/<int:id>/', CarDetailsView.as_view(), name='car_details'),
    path('delete/<int:id>/', DeletePostView.as_view(), name='delete_post'),
    path('buy_now/', BuyNowView.as_view(), name='buy_now'),
    # path('profile/', OrderHistoryView.as_view(), name='profile'),
    path('profile/',order_history,name='profile'),
    path('add_comment/<int:id>/', AddCommentView.as_view(), name='add_comment'),
]
