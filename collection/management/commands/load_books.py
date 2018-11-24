from django.core.management.base import BaseCommand
from djano.conf import settings
import os.path
import csv
from collection.models import Book
from django.core.files import File


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

# ORIGINAL COMMAND
    # def handle(self, *args, **options):
    #     print("Deleting books...")
    #     Book.objects.all().delete()
    #     with open(os.path.join(settings.BASE_DIR, 'initial_data',
    #                             'books.csv')) as file:
    #         reader = csv.DictReader(file)

    #         for row in reader:
            
    #             book = Book(
    #                 book_name=row['book_name'],
    #                 author=row['author'],
    #                 description=row['description']
    #             )
    #             book.save()
    #     print("Books loaded succesfully")


def handle(self, *args, **options):
        print("Deleting books...")
        Book.objects.all().delete()
        with open(get_path('books.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                book = Book(
                    book_name=row['book_name'],
                    author=row['author'],
                    description=row['description'],
                    pub_date=row['pub_date'],
                    python=row['python'],
                    css=row['css'],
                    html=row['html'],
                    javascript=row['javascript'],
                    slug=row['slug']
                )
                book.image.save(row['image'],
                                  File(open(get_path(row['image']), 'rb')))
                book.save()
        print(f"{i} books loaded!")


