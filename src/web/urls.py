from django.urls import path

# from .views import render_post
from web import views

urlpatterns = [
    # path("", render_post, name="home"),
    path("", views.home, name="home"),
    path("botones/", views.botones, name="botones"),
    path("about_us/", views.about_us, name="about_us"),
    path("start/", views.start, name="start"),
    path("start2/", views.start2, name="start2"),
]
