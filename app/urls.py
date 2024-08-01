from django.contrib import admin
from django.urls import path
from .views import TextDataApiView
urlpatterns = [
    path('', TextDataApiView.as_view(), name='api-view'),
]
