import json
import os

import django

# Налаштування Django для "плоскої" структури
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from quotes.models import Author, Quote


def load_data():
    # Завантаження авторів
    if os.path.exists('authors.json'):
        with open('authors.json', 'r', encoding='utf-8') as f:
            authors = json.load(f)
            for auth in authors:
                Author.objects.get_or_create(
                    fullname=auth['fullname'],
                    defaults={
                        'born_date': auth['born_date'],
                        'born_location': auth['born_location'],
                        'description': auth['description']
                    }
                )
        print("Authors migrated!")
    else:
        print("Error: authors.json not found!")

    # Завантаження цитат
    if os.path.exists('quotes.json'):
        with open('quotes.json', 'r', encoding='utf-8') as f:
            quotes = json.load(f)
            for q in quotes:
                author_obj = Author.objects.filter(fullname=q['author']).first()
                if author_obj:
                    Quote.objects.get_or_create(
                        quote=q['quote'],
                        author=author_obj,
                        tags=",".join(q['tags']) if isinstance(q['tags'], list) else q['tags']
                    )
        print("Quotes migrated!")
    else:
        print("Error: quotes.json not found!")

if __name__ == '__main__':
    load_data()