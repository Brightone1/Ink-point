from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<slug:slug>/reviews/', views.reviews, name='reviews')
]
