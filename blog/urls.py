from django.urls import path
from .views.views import hello_world


urlpatterns = [
    path('', hello_world, name='home'),
]