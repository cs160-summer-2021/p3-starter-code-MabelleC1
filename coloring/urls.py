from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('screen1', views.screen1, name='screen1'),
    path('createnew', views.createnew, name='createnew'),
    path('templates', views.templates, name='templates'),
    path('open', views.createnew, name='open'),
    path('new_interaction', views.index, name='new_interaction')
]
