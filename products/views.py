from django.db.models import Q 
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import OrderForm, CartForm
from .models import Product, Category, ImageUpload, SubCategory, User, Cart, Order
from django.contrib.auth.decorators import login_required


def index(request):
    """Home page"""
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'products/index.html', context)


def categories(request):
    """Show all product Categories"""
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'products/categories.html', context)


def subcategory(request, slug):
    """show each subcategory with its products"""
    subcategory = get_object_or_404(SubCategory, slug=slug)

    products = subcategory.product_set.all()
    context = {'subcategory': subcategory, 'products': products}
    return render(request, 'products/subcategory.html', context)


def product(request, slug):
    """Show individual product"""
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'products/product.html', context)



@login_required
def my_orders(request):
    """show all orders belonging to a specific user."""
    orders = Order.objects.filter(owner=request.user).order_by('-date_placed')
    order_count = orders.count()

    context = {'orders': orders, 'order_count': order_count}
    return render(request, 'products/my_orders.html', context)


@login_required
def new_order(request, slug):
    """Place a new order"""
    product = get_object_or_404(Product, slug=slug)

    if request.method != 'POST':
        # No data submitted: Show blank form
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        # Data submitted: process data
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.product = product
            new_order.owner = request.user
            new_order.save()
            return redirect('products:my_orders')

    context = {'form': form, 'product': product}
    return render(request, 'products/new_order.html', context)


@login_required
def cart(request):
    """show all cart-items"""
    cart_items = Cart.objects.filter(owner=request.user).order_by('-date_added')
    cart_item_count = cart_items.count()

    context = {'cart_items': cart_items, 'cart_item_count': cart_item_count}
    return render(request, 'products/cart.html', context)


@login_required
def add_to_cart(request, slug):
    """Add an item to cart"""
    product = get_object_or_404(Product, slug=slug)

    if request.method != 'POST':
        # No data submitted: Show blank form
        form = CartForm()
    else:
        form = CartForm(data=request.POST)
        # Data submitted: process data
        if form.is_valid():
            new_cart_item = form.save(commit=False)
            new_cart_item.product = product
            new_cart_item.owner = request.user
            new_cart_item.save()
            return redirect('products:cart')

    context = {'form': form, 'product': product}
    return render(request, 'products/add_to_cart.html', context)


@login_required
def delete_from_cart(request, cart_id):
    """Delete an item from cart"""
    cart_item = get_object_or_404(Cart, id=cart_id)

    if request.method == 'POST':
        # Data submitted: process data
        cart_item.delete()
        return redirect('products:cart')

    context = {'cart_item': cart_item}
    return render(request, 'products/delete_from_cart.html', context)


def search(request):
    """Search for items"""
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(name__icontains=query))
    search_count = products.count()

    context = {'products': products, 'query': query, 'search_count': search_count}
    return render(request, 'products/search.html', context)
