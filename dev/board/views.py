from django.shortcuts import render
from .models import Post


def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})
