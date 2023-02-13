import json
import os
from pathlib import Path
from django.core.files.base import ContentFile
import requests
from django.core.management import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Location, Image


def prepare_images(new_images_paths):
    images = []
    for img in new_images_paths:
        img_name = img.split('/')[-1]
        try:
            response = requests.get(img)
            response.raise_for_status()
            content = response.content
        except Exception as exc:
            print(f'Ошибка при скачивании картинки: {exc}')
            continue
        img_name_and_content = (img_name, content)
        images.append(img_name_and_content)
    return images


class Command(BaseCommand):
    def handle(*args, **options):
        new_places_jsons_path = Path(os.getcwd(), 'places-examples/places/')
        # new_media_jsons_path = Path(os.getcwd(), 'places-examples/media/')

        for address, dirs, files in os.walk(new_places_jsons_path):
            for json_file in files:
                json_file_path = os.path.join(address, json_file)
                with open(json_file_path, 'r') as ff:
                    readed_json_file = json.load(ff)
                    readed_images = readed_json_file['imgs']
                try:
                    create_location = Location.objects.get_or_create(
                        title=readed_json_file['title'],
                        description=readed_json_file['description_short'],
                        text=readed_json_file['description_long'],
                        latitude=readed_json_file['coordinates']['lng'],
                        longtitude=readed_json_file['coordinates']['lat'],
                    )

                    image_location = create_location[0]
                    print('image_location = ', image_location)

                    download_images = prepare_images(readed_images)
                    for download_image in download_images:
                        img_file_name = download_image[0]
                        img_content = ContentFile(download_image[1])

                        creat_image_model = Image.objects.get_or_create(
                            location=image_location,
                            image=img_file_name,
                        )
                        print('creat_image_model = ', creat_image_model)
                        save_image_to_model = creat_image_model[0].image.save(img_file_name, img_content, save=True)
                        print('save_image_to_model = ', save_image_to_model)

                except Location.DoesNotExist:
                    raise CommandError('Poll "%s" does not exist' % readed_json_file['title'])
