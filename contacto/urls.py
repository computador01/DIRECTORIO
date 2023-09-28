from django.urls import path
from .import views


urlpatterns = [
    path('add/', views.ContactoCreateView.as_view(),name="add"),
    path('delete/<pk>/', views.ContactoDeleteView.as_view(),name="delete"),
    path('update/<pk>/', views.ContactoUpdateView.as_view(),name="update"),
    path('listar_all', views.listar_all.as_view(),name="listar_all"),
    path('listar', views.listar.as_view(),name="listar"),
    path('detail/<pk>/', views.ContactoDetailView.as_view(),name="detail"),
    path('contacto/', views.ListContactosPdf.as_view(),name="contactos_all"),
]
