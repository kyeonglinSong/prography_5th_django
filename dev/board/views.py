from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm


def main(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'board/main.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})


def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(f'/post/{post.pk}')
    else:
        form = PostForm()
    return render(request, 'board/make_post.html', {'form': form})


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(f'/post/{post.pk}')
    else:
        form = PostForm(instance=post)
    return render(request, 'board/edit_post.html', {'form': form})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'board/delete_post.html', {'post': post})


def add_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'/post/{post.pk}')
    else:
        form = CommentForm()
    return render(request, 'board/add_comment.html', {'form': form})
