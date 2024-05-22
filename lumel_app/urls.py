from django.urls import path
from .views import MainView

app_name = 'lumel_app'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
