from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/article_list.html'
    

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name ='articles/article_detail.html'

class ArticleUpdateView(UserPassesTestMixin ,LoginRequiredMixin,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin ,LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title','body')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Create your views here.
