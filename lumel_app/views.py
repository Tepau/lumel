from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Article


class MainView(FormView):
    template_name = "main.html"
    form_class = ContactForm
    success_url = reverse_lazy('lumel_app:main')

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = "articles.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "article.html"
    model = Article
