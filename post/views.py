from django.shortcuts import render
from .models import Post, Tag, Category
from django.shortcuts import get_object_or_404


def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post}
    return render(request=request, template_name=post.get_template_name(), context=context)


def latest_posts(request):
    posts = Post.objects.all().order_by("-created_at")[:5]
    return render(request, "latest-posts.html", {"posts": posts})
# Also add a Django Template widget to get the latest posts
# Option 1: Add as REST => Add in JS
# Option 2: Add as widget and view


# def recommendations(request):
# recommend posts from user session: ML
