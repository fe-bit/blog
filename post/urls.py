
from django.urls import path
from .views import detail_post, latest_posts

urlpatterns = [
    path("latest-posts/", latest_posts, name="latest-posts"),
    path("<slug:slug>/", detail_post, name="detail-post"),
]
