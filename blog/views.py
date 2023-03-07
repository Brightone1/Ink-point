from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Content, Comment
from .forms import CommentForm

def topics(request):
	"""Show all blogs"""
	topics = Topic.objects.all()
	context = {'topics': topics}
	return render(request, 'blog/topics.html', context)


def topic(request, slug):
	"""Show individual blog"""
	topic = get_object_or_404(Topic, slug=slug)
	contents = topic.content_set.all()
	context = {'topic': topic, 'contents': contents}
	return render(request, 'blog/topic.html', context)


def content(request, content_id):
	"""Show individual content and its comments"""
	content = get_object_or_404(Content, id=content_id)
	comments = Comment.objects.order_by('-date_published')

	if request.method != "POST":
		# No data: display blank page
		form = CommentForm()

	else:
		# Data submitted: process data
		form = CommentForm(data=request.POST)
		if form.is_valid:
			new_comment = form.save(commit=False)
			new_comment.content = content
			new_comment.save()
			return redirect('blog:content', content_id=content_id)

	context = {'comments': comments, 'content': content, 'form': form}
	return render(request, 'blog/content.html', context)
