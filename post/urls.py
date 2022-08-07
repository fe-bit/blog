
from django.urls import path
from .views import detail_post

urlpatterns = [
    path("<slug:slug>/", detail_post, name="detail-post"),
]
