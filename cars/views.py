# from django.shortcuts import render,redirect
# from . import forms
# from . import models
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, render
# from .models import Post,Order,Comment
# from django.contrib import messages
# # Create your views here.

# @login_required
# def add_post(request):
#     if request.method=='POST':
#         post_form=forms.PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save(commit=False)  # Create a new Post object but don't save to database yet
#             new_post.author = request.user  # Assign the author
#             new_post.save()  # Save the post with the assigned author
#             return redirect('add_post')
#     else:
#         post_form=forms.PostForm()
#     return render(request, 'add_post.html',{'form':post_form})

# @login_required
# def edit_post(request,id):
#     # post model er instance (/object/children) dakhte parbe ! 

#     post=models.Post.objects.get(pk=id)
#     # print(post)
#     post_form=forms.PostForm(instance=post)

#     if request.method=='POST':
#         post_form=forms.PostForm(request.POST,instance=post)
#         # user kno kichu change na krle instance... !
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect('homepage')
#     return render(request, 'add_post.html',{'form':post_form})


# def car_details(request, id):
#     post = get_object_or_404(Post, pk=id)
#     return render(request, 'car_details.html', {'car': post})

# @login_required
# def delete_post(request,id):
#     post=models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect('homepage')
# @login_required
# def buy_now(request):
#     if request.method == 'POST' and request.user.is_authenticated:
#         car_id = request.POST.get('car_id')
#         if car_id:
#             # Get the car object
#             car = Post.objects.get(id=car_id)
#             # Create a new order for the current user
#             Order.objects.create(car=car, user=request.user)
#             # Decrease the car quantity
#             car.car_quantity -= 1
#             car.save()
#     return redirect('profile')  # Redirect to order history page or user profile

# @login_required
# def order_history(request):
#     orders = Order.objects.filter(user=request.user)
#     context = {'orders': orders}
#     print(context)
#     return render(request, 'profile.html', context)


# @login_required
# def add_comment(request, id):
#     if request.method == 'POST':
#         car = Post.objects.get(pk=id)
#         name = request.POST['name']
#         comment_text = request.POST['comment']
#         Comment.objects.create(car=car, user=request.user, name=name, comment=comment_text)
#         messages.success(request, 'Comment added successfully!')
#         return redirect('car_details', id=id)  # Redirect to car details using 'id' parameter
#     else:
#         return redirect('homepage')  # Redirect to home page if not a POST request

# convert into class vased view : 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from .models import Post, Order, Comment
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class AddPostView(View):
    @login_required
    def get(self, request):
        post_form = PostForm()
        return render(request, 'add_post.html', {'form': post_form})
    
    @login_required
    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('add_post')
        return render(request, 'add_post.html', {'form': post_form})

class EditPostView(View):
    @login_required
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post_form = PostForm(instance=post)
        return render(request, 'add_post.html', {'form': post_form})
    
    @login_required
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
        return render(request, 'add_post.html', {'form': post_form})

class CarDetailsView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        return render(request, 'car_details.html', {'car': post})

class DeletePostView(View):
    @login_required
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return redirect('homepage')

class BuyNowView(LoginRequiredMixin, View):
    def post(self, request):
        if request.user.is_authenticated:
            car_id = request.POST.get('car_id')
            if car_id:
                car = get_object_or_404(Post, id=car_id)
                Order.objects.create(car=car, user=request.user)
                car.car_quantity -= 1
                car.save()
        return redirect('profile')

# class OrderHistoryView(View):
#     @login_required
#     def get(self, request):
#         orders = Order.objects.filter(user=request.user)
#         context = {'orders': orders}
#         return render(request, 'profile.html', context)

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    print(context)
    return render(request, 'profile.html', context)


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, id):
        if request.user.is_authenticated:
            car = get_object_or_404(Post, pk=id)
            name = request.POST.get('name')
            comment_text = request.POST.get('comment')
            Comment.objects.create(car=car, user=request.user, name=name, comment=comment_text)
            messages.success(request, 'Comment added successfully!')
            return redirect('car_details', id=id)
        return redirect('homepage')