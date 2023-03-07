from django.contrib import admin
from .models import Blog, Entry


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'owner', 'date_added']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry)

