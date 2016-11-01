from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ['name', 'timestamp', 'updated_time','category']
    list_display_links = ['name']
    search_fields = ['name', 'article']
    list_filter = ['updated_time', 'author', 'category']

admin.site.register(Article, ArticleModelAdmin)