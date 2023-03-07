from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Search
    path('search/', views.search, name='search'),

    # Product Categories
    path('categories/', views.categories, name='categories'),

    # subcategory products
    path('subcategories/<slug:slug>/', views.subcategory, name='subcategory'),

    # Product
    path('products/<slug:slug>/', views.product, name='product'),

    # Show all user orders
    path('my_orders/', views.my_orders, name='my_orders'),

    # Place new order
    path('<slug:slug>/new_order/', views.new_order, name='new_order'),

    # Show all items in cart
    path('cart/', views.cart, name='cart'),

    # Add a new item to cart
    path('<slug:slug>/add_to_cart/', views.add_to_cart, name='add_to_cart'),

    # Delete an item from cart
    path('cart/<int:cart_id>/delete_from_cart/', views.delete_from_cart, name='delete_from_cart'),

]
