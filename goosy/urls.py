from django.urls import path
from . import views

urlpatterns = [
    # URL + function name from views.py
    path('tracks/', views.list_tracks),
    path('tracks/<int:pk>/', views.detail_track),
]