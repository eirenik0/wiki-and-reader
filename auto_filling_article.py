import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
from django.core.management import execute_from_command_line
execute_from_command_line(['--settings=config.settings.local'])

from wiki_allatra_club.reader.models import BookModel
from wiki.models.urlpath import Article, URLPath, ArticleRevision
from wiki_allatra_club.users.models import User
from slugify import slugify


from django.core.exceptions import ObjectDoesNotExist


def create_update_slug():
    books = BookModel.objects.all()
    for book in books:
        book.slug = slugify(book.title)
        book.save()

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def create_alphabetic_urls(url_slug='ru'):
    urlpath = URLPath.objects.get(slug=url_slug)
    user = User.objects.get(username='admin')
    article = Article.objects.get(urlpath=urlpath)
    for char in ALPHABET:
        try:
            URLPath.objects.get(slug=slugify(char))
        except ObjectDoesNotExist:
             URLPath.create_article(
                urlpath,
                slugify(char),
                title=char.upper(),
                content='',
                user_message='',
                user=user,
                ip_address=None,
                article_kwargs={'owner': user,
                                'group': article.group,
                                'group_read': article.group_read,
                                'group_write': article.group_write,
                                'other_read': article.other_read,
                                'other_write': article.other_write,
                                })

if __name__=='__main__':
    create_alphabetic_urls()