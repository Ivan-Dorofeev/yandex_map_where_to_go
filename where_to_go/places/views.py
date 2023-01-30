from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from places.models import Location
from places.models import Image


def places(request, place_id):
    place = get_object_or_404(Location, id=place_id)
    images = Image.objects.filter(location=place)

    context = {
        "title": place.title,
        "imgs": [img.image.url for img in images],
        "description_short": place.description,
        "description_long": place.text,
        "coordinates": {
            "lng": place.longtitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(context, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
