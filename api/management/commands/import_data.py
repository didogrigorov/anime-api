from django.core.management.base import BaseCommand, CommandError
import csv

from api.models import Anime


class Command(BaseCommand):
    help = "Import data function"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('data/anime.csv', newline='') as csvfile:
            animes = csv.DictReader(csvfile)
            # for row in animes:
            #     Anime.objects.create(
            #         name = row['name'],
            #         genre = row['genre'],
            #         type = row['type'],
            #         episodes= row['episodes'],
            #         rating = row['rating'],
            #         members = row['members']
            #     )
            anime_objects = []
            for row in animes:
                anime_objects.append(Anime(
                    name=row['name'],
                    genre=row['genre'],
                    type=row['type'],
                    episodes=row['episodes'],
                    rating=row['rating'],
                    members=row['members'],
                ))

            # create instances and return a queryset of the created items
            animes = Anime.objects.bulk_create(anime_objects, batch_size=len(anime_objects))