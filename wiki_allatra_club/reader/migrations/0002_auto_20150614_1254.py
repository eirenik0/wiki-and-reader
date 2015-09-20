# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wiki_allatra_club.reader.models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='book',
            field=models.FileField(verbose_name='book file', upload_to='books/books', validators=[wiki_allatra_club.reader.models.validate_epub]),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(verbose_name='cover', upload_to='books/covers', default='books/covers/defaults.png'),
        ),
    ]
