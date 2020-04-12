from django.urls import path
from project import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectDetail.as_view()),
    #change to viewset
    ]

