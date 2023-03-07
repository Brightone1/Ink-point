"""Contains the URL patterns for the notebox app"""

from django.urls import path
from . import views

app_name = 'notebox'

urlpatterns = [

    # Blogs page
    path('subjects/', views.blogs, name="blogs"),

    # Each blog page
    path('subjects/<int:blog_id>/', views.blog, name="blog"),

    # Delete subject
    path('subjects/<int:blog_id>/delete_subject/', views.delete_subject, name="delete_subject"),

    # new blog page
    path('new_subject/', views.new_blog, name="new_blog"),

    # new Entry page
    path('<int:blog_id>/new_note/', views.new_entry, name="new_entry"),

    # Edit Entry page
    path('<int:entry_id>/edit_note/', views.edit_entry, name="edit_entry"),

]
