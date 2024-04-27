from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Post,Order
# Create your views here.

@login_required
def add_post(request):
    if request.method=='POST':
        post_form=forms.PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)  # Create a new Post object but don't save to database yet
            new_post.author = request.user  # Assign the author
            new_post.save()  # Save the post with the assigned author
            return redirect('add_post')
    else:
        post_form=forms.PostForm()
    return render(request, 'add_post.html',{'form':post_form})

@login_required
def edit_post(request,id):
    # post model er instance (/object/children) dakhte parbe ! 

    post=models.Post.objects.get(pk=id)
    # print(post)
    post_form=forms.PostForm(instance=post)

    if request.method=='POST':
        post_form=forms.PostForm(request.POST,instance=post)
        # user kno kichu change na krle instance... !
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('homepage')
    return render(request, 'add_post.html',{'form':post_form})


def car_details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'car_details.html', {'car': post})

@login_required
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

def buy_now(request):
    if request.method == 'POST' and request.user.is_authenticated:
        car_id = request.POST.get('car_id')
        if car_id:
            # Get the car object
            car = Post.objects.get(id=car_id)
            # Create a new order for the current user
            Order.objects.create(car=car, user=request.user)
            # Decrease the car quantity
            car.car_quantity -= 1
            car.save()
    return redirect('profile')  # Redirect to order history page or user profile

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    print(context)
    return render(request, 'profile.html', context)



