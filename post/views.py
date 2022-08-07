from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.


def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post}
    return render(request=request, template_name=post.get_template_name(), context=context)
