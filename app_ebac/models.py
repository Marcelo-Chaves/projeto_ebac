from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Modelo Usuario com campos extras
class Usuario(AbstractUser):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Verificar se o slug não foi fornecido
        if not self.slug:
            base = slugify(self.username)
            slug = base
            count = 1

            # Garantir que o slug seja único
            while Usuario.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                count += 1
                slug = f"{base}-{count}"

            self.slug = slug

        # Chamar o método save() da classe pai (AbstractUser)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


# Modelo Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Gerar o slug automaticamente se não fornecido
        if not self.slug:
            base = slugify(self.title)  # Aqui estamos gerando o slug com base no título do post
            slug = base
            count = 1

            # Garantir que o slug seja único
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                count += 1
                slug = f"{base}-{count}"

            self.slug = slug

        # Chamar o método save() da classe pai (Model)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
