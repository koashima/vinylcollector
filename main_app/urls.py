from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.VinylList.as_view(), name='vinyls_index'),
    path('vinyls/<int:pk>/', views.vinyl_detail, name='vinyls_detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:pk>/add_listening/', views.add_listening, name='add_listening'),
    path('contributors/', views.ContributorList.as_view(), name='contributors_index'),
    path('vinyls/<int:pk>/', views.ContributorDetail.as_view(), name='contributors_detail'),
    # path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    # path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    # path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    # path('vinyls/<int:pk>/add_listening/', views.add_listening, name='add_listening'),
]
