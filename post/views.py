from django.shortcuts import render
from .models import Post, Tag, Category
from django.shortcuts import get_object_or_404

# Create your views here.


def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post}
    return render(request=request, template_name=post.get_template_name(), context=context)


# Transform to Django Template widget
def latest_posts(request):
    posts = Post.objects.all().order_by("-created_at")[:5]
    return render(request, "latest-posts.html", {"posts": posts})
