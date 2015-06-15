from wiki_allatra_club.reader.models import BookModel

def get_books(request):
    context = {}
    context['books_list'] = BookModel.objects.all().order_by('title')
    return context