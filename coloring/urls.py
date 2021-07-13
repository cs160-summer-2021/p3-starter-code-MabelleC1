from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('home', views.home, name='home'),
    path('drawing', views.drawing, name='drawing'),
    path('templates', views.templates, name='templates'),
    path('templates/animals', views.animals, name='animals'),
    path('templates/abstract', views.abstract, name='abstract'),
    path('templates/error', views.error, name='error'),
    path('open', views.open, name='open'),
    path('new_interaction', views.index, name='new_interaction')
]
