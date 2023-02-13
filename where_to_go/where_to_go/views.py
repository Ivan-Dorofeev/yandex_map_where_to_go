from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from places.models import Location


def main(request):
    locations = Location.objects.all()

    features = []
    for location in locations:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [location.latitude, location.longtitude]
                },
                "properties": {
                    "title": location.title,
                    "placeId": location.id,
                    "detailsUrl": reverse('places', args=[location.id])
                }
            })
    context = {
        'geo_data': {
            "type": "FeatureCollection",
            "features": features
        }
    }

    return render(request, 'index.html', context)
