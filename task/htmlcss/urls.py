from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add, name='add'),
    path('regis',views.regis, name='regis'),
    path('main',views.main, name='main')
]