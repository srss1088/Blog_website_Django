from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def About(requ/st):
    # return render(request, 'about.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class About(ListView):
    model = Post
    template_name = 'about.html'
