from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Article

# Register your models here.

# Apply summernote to Article.body TextField in model.
class ArticleAdmin(SummernoteModelAdmin):  # inherits from ModelAdmin
    summernote_fields = ('body',)
    list_display = ('title', 'date', 'views',)
    list_filter = ('date', )
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Article, ArticleAdmin)