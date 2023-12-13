from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main),
    path('stosa/', views.stosa),
    path('asialines/', views.asialines),
    path('bc-crm/', views.bc_crm),
    path('bc-mp/', views.bc_mp),
    path('caravan/', views.caravan),
    path('dega/', views.dega),
    path('macdoner/', views.macdoner),
    path('mac-mp/', views.mac_mp),
    path('thearch/', views.thearch),
]
