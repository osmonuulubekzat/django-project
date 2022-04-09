from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", 'publishingdate']
    list_filter = ['publishingdate']
    search_fields = ["title", 'content']
    class Meta:
        model = Blog
admin.site.register(Blog,BlogAdmin)
