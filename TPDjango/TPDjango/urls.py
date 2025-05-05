from django.contrib import admin
from django.urls import path
from AppDJANGO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.connexion, name='accueil'),  
    path('connexion/', views.connexion, name='connexion'),
    path('listeEvent/', views.listeEvent, name='listeEvent'),
    path('detailevent/<int:event_id>/', views.detailevent, name='detailevent'),
    path('participer_evenement/<int:event_id>/participer/', views.participer_evenement, name='participer_evenement'),
]


