'''

'''

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
    '''
    create slug for book from title, need only for earlier saved books
    :return:
    '''
    books = BookModel.objects.all()
    for book in books:
        book.slug = slugify(book.title)
        book.save()

ALPHABET = 'абвгдежзийклмнопрстуфхцчшщэюя'
KEYWORDS = ['аллат', 'Адви', 'Алатырь-камень', 'АллатРа', 'Алтарь', 'Альфа-ритм', 'бета-ритм', 'аниматизм', 'апсида',
            'Аскет', 'Ахура Мазда', 'айны'
            'Бамбара', 'Баота', 'Басуто', 'Благо',
            'Вишну', 'Воля', 'Вритра', 'Гипоталамус', 'Дагоба', 'вуду',
            'Дагомея', 'Дева Мария', 'Догоны', 'Дохристианская славянская мифология', 'Древнекитайская мифология',
            'Евхаристия',
            'Звездчатый октаэдр', 'Золотые таблички Тота',
            'Изначальный звук', 'Иисус Христос', 'Икона «Богородица Оранта»', 'Икона «Неопалимая Купина»',
            'Икона «Спас в Силах»', 'Индра (Индрик)', 'Исида', 'Ишвара',
            'Каббала', 'Кали (век кали)', 'Квадрифолий', 'Киевская Русь', 'Койсанские щелкающие языки', 'Крабовидная туманность',
            'Кундалини',
            'Легенды о сотворении мира', 'Личность, субличность',
            'Мандала', 'Масса', 'Материя', 'Медитация «Пирамида»', 'Медитация «Четверик»', 'Мирра', 'Михраб', 'Многоуровневость сознания',
            'Монада',
            'Навахо', 'Нейронная звезда', 'Неопалимая купина',
            'Оранта', 'Осирис', 'Остров Пасхи', 'Откровения Иоанна Богослова',
            'Параллельные миры', 'Покой', 'Полуправильные многогранники', 'Пурана',
            'реинкарнация', 'Ретикулярные клетки', 'Ромб',
            'Свастика', 'Сексуальная энергия', 'Сиддхи', 'Символ', 'Скипетр, посох', 'Славянские шатровые постройки', 'Слипер',
            'Софийский Собор', 'Спираль', 'Стрибог', 'Суд Осириса', 'Сутра', 'Суфизм',
            'Таламус', 'Тела Хладни', 'Толпа (поведение людей в толпе)', 'Тотемизм', 'Трон',
            'Уроборос',
            'Фарь', 'Фетишизм', 'Фрактал',
            'Хара', 'Христианство, семь таинств (ступени развития)',
            'Цилинь (единорог)', 'Чакра', 'Черные дыры', 'Чувства', 'Шатер',
            'Электрон', 'Эмоции', 'Энергетическая структура человека', 'Янтра', 'Ярослав Мудрый'
]

def create_article():
    pass

# def create_

def create_alphabetic_urls(url_slug='ru'):
    '''
    generate alphabetic table of content for selected language
    :param url_slug:
    :return:
    '''
    urlpath = URLPath.objects.get(slug=url_slug)
    user = User.objects.get(username='admin')
    article = Article.objects.get(urlpath=urlpath)
    for char in ALPHABET:
        try:
            URLPath.objects.get(slug=char)
        except ObjectDoesNotExist:
             URLPath.create_article(
                urlpath,
                char,
                title=char.upper(),
                content='[article_list depth:2]',
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