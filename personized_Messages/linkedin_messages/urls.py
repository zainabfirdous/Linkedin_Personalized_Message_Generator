from django.urls import path
from .Controller.Posts import get_posts

urlpatterns = [
    path('', get_posts, name="getter"),
]