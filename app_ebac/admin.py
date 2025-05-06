from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Post

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('title', 'content', 'slug')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais', {'fields': ('title', 'content', 'slug')}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'title', 'slug')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    prepopulated_fields = {'slug': ('title',)}
