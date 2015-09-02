from wiki_allatra_club.reader.models import BookModel

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

