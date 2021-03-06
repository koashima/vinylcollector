from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.VinylList.as_view(), name='vinyls_index'),
    path('vinyls/<int:pk>/', views.vinyl_detail, name='vinyls_detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:pk>/add_listening/', views.add_listening, name='add_listening'),

    path('contributors/', views.ContributorList.as_view(), name='contributors_index'),
    path('contributors/<int:pk>/', views.ContributorDetail.as_view(), name='contributors_detail'),
    path('contributors/create/', views.ContributorCreate.as_view(), name='contributors_create'),
    path('contributors/<int:pk>/update/', views.ContributorUpdate.as_view(), name='contributors_update'),
    path('contributors/<int:pk>/delete/', views.ContributorDelete.as_view(), name='contributors_delete'),
    path('contributors/<int:pk>/', views.ContributorDetail.as_view(), name='contributors_detail'),
    path('vinyls/<int:vinyl_id>/assoc_contributor/<int:contributor_id>/', views.assoc_contributor, name='assoc_contributor'),
    path('vinyls/<int:vinyl_id>/unassoc_contributor/<int:contributor_id>', views.unassoc_contributor, name='unassoc_contributor'),  
    path('accounts/signup/', views.signup, name='signup'),
    path('chat/', include('chat.urls')),
]
