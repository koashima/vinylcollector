from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.VinylList.as_view(), name='vinyls_index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_details, name='vinyls_detail'),
]
