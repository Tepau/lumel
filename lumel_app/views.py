from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm


class MainView(FormView):
    template_name = "main.html"
    form_class = ContactForm
    success_url = reverse_lazy('lumel_app:main')

    def form_valid(self, form):
        print('Formulaire ok')

        return super().form_valid(form)