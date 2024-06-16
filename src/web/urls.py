from django.urls import path

# from .views import render_post
from web import views

urlpatterns = [
    # path("", render_post, name="home"),
    path("", views.home, name="home"),
    path("botones/", views.botones, name="botones"),
    path("about_us/", views.about_us, name="about_us"),
]
