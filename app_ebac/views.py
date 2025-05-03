from django.shortcuts import render
from .models import Post
# Create your views here.

def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'app_ebac/listar_posts.html', {'posts': posts})

