from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url='login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url='login'
    fields = ['comment']

class ArticleUpdateView(LoginRequiredMixin,UpdateView,):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'article_update.html'
    login_url='login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = models.Article
    template_name = 'article_create.html'
    fields = ['title', 'body',]
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleComment(LoginRequiredMixin,CreateView):
    model = models.Comment
    template_name = 'article_comment.html'
    fields = ['comment',]
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
