import csv

from django.core.management.base import BaseCommand
from django.http import HttpResponse
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('2.1-databases/work_with_database/phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                # Используем get_or_create для проверки существования и создания
                Phone.objects.update_or_create(
                    id=phone['id'],  # Уникальное значение для проверки
                    defaults={
                        'name': phone['name'],
                        'image': phone['image'],
                        'price': int(phone['price']),
                        'release_date': phone['release_date'],
                        'lte_exists': phone['lte_exists'],
                        'slug': slugify(phone['name']),  # Создаем slug из имени
                    }
                )
