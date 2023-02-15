from django.urls import path

from places.views import main, places

urlpatterns = [
    path('', main, name='main'),
    path('<int:place_id>/', places, name='places'),
]

