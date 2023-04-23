from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('words/', views.getWords, name="words"),
    path('words/<str:pk>/', views.getWord, name="word"),
    path('lessons/', views.getLessons, name='lessons'),
    path('lessons/<str:pk>/', views.getLesson, name='lesson'),
]
