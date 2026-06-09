from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:pk>/', views.edit_url, name='edit_url'),
    path('delete/<int:pk>/', views.delete_url, name='delete_url'),
    path('s/<str:short_key>/', views.redirect_url, name='redirect_url'),
]
