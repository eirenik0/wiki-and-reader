from collections import namedtuple

from wiki_allatra_club.reader.models import BookModel
from wiki.models.urlpath import URLPath

from taggit.models import Tag


def get_books(request):

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i+n]

    context = {}
    books = BookModel.objects.all().order_by('id')
    context['books_list'] = books
    context['books_chunked_list'] = chunks(books, 2)
    return context

def get_url_children(request, url_slug='ru'):
    url_children = URLPath.objects.get(slug=url_slug).get_children()
    Url = namedtuple('Url', 'path char')
    context = {}
    context['url_children'] = (Url(path=url.path, char=url.slug.upper()) for url in url_children)
    return context

def get_tags(request):
    tags = Tag.objects.all()
    Tag_nt = namedtuple('Tag', 'name num_times url')
    context = {}
    context['tags'] = (Tag_nt(name=tag.name,
                              num_times=tag.taggit_taggeditem_items.count(),
                              url='_tag/?query={}'.format(tag.name))
                       for tag in tags)
    return context