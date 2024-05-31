from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Article


class MainView(FormView):
    template_name = "main.html"
    form_class = ContactForm
    success_url = reverse_lazy('lumel_app:main')

    def form_valid(self, form):
        form_data = form.cleaned_data
        message = f"Nom: {form_data['nom']}\nTéléphone: {form_data['telephone']}\nEmail: {form_data['email']}\nDate: {form_data['date']}\nHeure: {form_data['heure']}\nMessage: {form_data['message']}"
        send_mail(
            'Nouveau message de contact via lumel-associees.fr',
            message,
            settings.EMAIL_HOST_USER,
            ['lumel-associees@outlook.fr'],
            fail_silently=False,
        )

        # Appel de la méthode form_valid de la classe parente pour poursuivre le traitement
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = "articles.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "article.html"
    model = Article
