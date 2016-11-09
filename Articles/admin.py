from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ['name', 'timestamp', 'updated', 'category']
    list_display_links = ['name']
    search_fields = ['name', 'article']
    list_filter = ['category', 'timestamp']
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'category', 'content']}),
        ('Image information', {'fields': ['image','height_field','width_field']}),
        ('Author(s) information', {'fields': ['author']}),
    ]

admin.site.register(Article, ArticleModelAdmin)