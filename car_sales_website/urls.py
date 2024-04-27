from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('post/', include('cars.urls')),
    path('category/', include('brands.urls')),
    path('', views.home, name='homepage'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
]