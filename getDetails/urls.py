from django.urls import path, include
from .views import PinDetails


urlpatterns = [
    path('details', PinDetails),
]
