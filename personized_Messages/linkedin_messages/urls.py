from django.urls import path
from .Controller.Posts import get_posts
from .Controller.Message import generateMsg
urlpatterns = [
    path('', get_posts, name="getter"),
    path('generate', generateMsg, name="generation")
]