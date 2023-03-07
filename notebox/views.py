from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . models import Blog, Entry
from .forms import BlogForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def blogs(request):
    """Show all blogs."""
    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'notebox/blogs.html', context)


@login_required
def blog(request, blog_id):
    """show Individual Blog with its content"""
    blog = get_object_or_404(Blog, id=blog_id)

    # Make sure the topic belongs to the current user.
    if blog.owner != request.user:
        raise Http404

    entries = blog.entry_set.order_by('-date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'notebox/blog.html', context)


@login_required
def delete_subject(request, blog_id):
    """show Individual Blog with its content"""
    blog = get_object_or_404(Blog, id=blog_id)

    # Make sure the topic belongs to the current user.
    if blog.owner != request.user:
        raise Http404

    if request.method == 'POST':
        blog.delete()
        return redirect('notebox:blogs')

    context = {'blog': blog}
    return render(request, 'notebox/delete_subject.html', context)


@login_required
def new_blog(request):
    """Add new blog"""

    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('notebox:blogs')

    context = {'form': form}
    return render(request, 'notebox/new_blog.html', context)


@login_required
def new_entry(request, blog_id):
    """Add new entry"""
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            return redirect('notebox:blog', blog_id=blog_id)

    context = {'blog': blog, 'form': form}
    return render(request, 'notebox/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit entry"""
    entry = get_object_or_404(Entry, id=entry_id)
    blog = entry.blog

    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notebox:blog', blog_id=blog.id)

    context = {'entry': entry, 'blog': blog, 'form': form}
    return render(request, 'notebox/edit_entry.html', context)
