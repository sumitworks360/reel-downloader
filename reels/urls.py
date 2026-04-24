from django.urls import path
from .views import download_reel


urlpatterns = [
    path('download/', download_reel),
]

