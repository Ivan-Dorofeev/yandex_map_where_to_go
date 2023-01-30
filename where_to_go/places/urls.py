from django.urls import path, include

from places import views

urlpatterns = [
    path('<int:place_id>/', views.places, name='places'),
]
