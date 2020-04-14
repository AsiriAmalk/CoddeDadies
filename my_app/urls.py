from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('new_serch/', views.new_search, name='new_search'),
    path('', views.home, name='home'),
    path('index', views.index, name='index')
]