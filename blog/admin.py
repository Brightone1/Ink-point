from django.contrib import admin
from .models import Topic, Content, Comment

class TopicAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Topic, TopicAdmin)
admin.site.register(Content)
admin.site.register(Comment)
