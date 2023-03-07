from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def reviews(request, slug):
    """Show all reviews"""
    product = get_object_or_404(Product, slug=slug)
    reviews = Review.objects.order_by('-date_posted')

    if request.method != 'POST':
        # No data submitted: show blank form
        form = ReviewForm()
    else:
        # Data submitted: process data
        form = ReviewForm(data=request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('reviews:reviews', slug=slug)

    context = {'reviews': reviews, 'form': form, 'product': product}
    return render(request, 'reviews/reviews.html', context)
