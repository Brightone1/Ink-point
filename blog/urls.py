"""Contains URL patterns for the blog app"""

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
# Show all blogs
path('blogs/', views.topics, name="topics"),

# show individual blog
path('blogs/<slug:slug>/', views.topic, name="topic"),

# Show each blog content
path('content/<int:content_id>/', views.content, name="content"),

]