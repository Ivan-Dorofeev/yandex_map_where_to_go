from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from places.models import Location, Image
from django.db import connection


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
