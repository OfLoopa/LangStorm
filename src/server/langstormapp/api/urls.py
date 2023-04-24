from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('words/', views.getWords, name="words"),
    path('words/<str:pk>/', views.getWord, name="word"),
    path('dictionaries/', views.getDictionaries, name="dictionaries"),
    path('dictionaries/<str:pk>/', views.getDictionary, name="dictionary"),
    path('lessons/', views.getLessons, name='lessons'),
    path('lessons/<str:pk>/', views.getLesson, name='lesson'),
]
