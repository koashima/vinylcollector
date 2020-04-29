from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_details, name='detail'),
]
