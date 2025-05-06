from django.shortcuts import render, get_object_or_404
from .models import Post

# Função para listar todos os posts (opcional, pode ser removida se você usar apenas 'home_view')
def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'app_ebac/index.html', {'post_list': posts})

# Função para a página home, que lista todos os posts
def home_view(request):
    post_list = Post.objects.all()  # Obtenha todos os posts
    return render(request, 'app_ebac/index.html', {'post_list': post_list})

# Função para exibir detalhes de um post específico com base no slug
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'app_ebac/post_detail.html', {'post': post})
