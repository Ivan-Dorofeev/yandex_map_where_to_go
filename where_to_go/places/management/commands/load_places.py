import json
import os
from pathlib import Path
import requests
from django.core.management import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Location, Image

from where_to_go.settings import BASE_DIR


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
        images.append((img_name, content))
    return images


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            nargs='+',
            type=str,
            help='Указывается путь откуда будут будут браться JSON файлы. По умолчанию из places_and_pictures/places/'
        )

    def handle(self, *args, **options):
        base_dir = BASE_DIR.resolve().parent
        new_places_jsons_path = os.path.join(base_dir, 'places_and_pictures/places/')
        if options['path']:
            try:
                new_places_jsons_path = os.path.join(base_dir, str(options['path'][0]))
            except Exception as exc:
                print('Проблемы с указанием пути для JSON файла: ', exc)

        for address, dirs, files in os.walk(new_places_jsons_path):
            for json_file in files:
                json_file_path = os.path.join(address, json_file)
                with open(json_file_path, 'r') as json_file:
                    read_json_file = json.load(json_file)
                    read_images = read_json_file['imgs']
                try:
                    place, created = Location.objects.get_or_create(
                        title=read_json_file['title'],
                        defaults={
                            'short_description': read_json_file['description_short'],
                            'long_description': read_json_file['description_long'],
                            'latitude': read_json_file['coordinates']['lng'],
                            'longtitude': read_json_file['coordinates']['lat']
                        }
                    )

                    download_images = prepare_images(read_images)
                    for number, download_image in enumerate(download_images):
                        img_file_name = download_image[0]
                        img_content = ContentFile(download_image[1])

                        created_image_model = Image.objects.get_or_create(
                            index=number,
                            location=place,
                            image=img_file_name,
                        )
                        created_image_model[0].image.save(img_file_name, img_content, save=True)

                except Location.DoesNotExist:
                    raise CommandError('Location does not exist: "%s"' % read_json_file['title'])
