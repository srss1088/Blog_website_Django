# from . import views
from django.urls import path
from .views import HomeView, ArticleDetailView, About
urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('about', About.as_view(), name="about")
]