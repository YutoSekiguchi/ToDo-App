from django.urls import path
from django.views.generic.base import View
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
