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
        (None, {'fields': ['name', 'content', 'category']}),
        ('Author(s)', {'fields': ['author']}),
        # ('Date Information', {'fields': ['updated','timestamp']})
    ]

admin.site.register(Article, ArticleModelAdmin)