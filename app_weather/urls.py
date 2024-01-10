from django.urls import path
from .views import my_view
from .views import weather_view

urlpatterns = [
    # path('weather/', my_view),
    path('weather/', weather_view)
]