from django.urls import path

from places.views import places


urlpatterns = [
    path('<int:place_id>/', places, name='places'),
]

