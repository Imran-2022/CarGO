from django.shortcuts import render
from cars.models import Post
from brands.models import Category
# Create your views here.

def home(request,category_slug=None):
    data = Post.objects.all()
    # print(data)
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        data = Post.objects.filter(brand=category)

    categories=Category.objects.all()
    return render(request,'home.html',{'data':data,'category':categories})
