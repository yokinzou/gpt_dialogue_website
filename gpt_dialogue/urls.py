from django.urls import path
from . import views

urlpatterns = [
    path('dialogue/', views.dialogue, name='dialogue'),
]
