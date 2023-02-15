from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Location, Image


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


def places(request, place_id):
    place = get_object_or_404(Location, id=place_id)
    images = place.images.all()

    context = {
        "title": place.title,
        "imgs": [img.image.url for img in images],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longtitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(context, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
