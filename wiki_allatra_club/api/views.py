import django_filters
from rest_framework import viewsets

from wiki.plugins.annotations.models import AnnotationModel

from .serializers import AnnotationSerializer


from django.http import JsonResponse
from epubsearcher import EpubWorker
from wiki_allatra_club.reader.models import BookModel, ChapterBookModel


class AnnotationFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(
        name='books__title',
        lookup_type='contains',
    )
    book_id = django_filters.CharFilter(
        name='books__id',
        lookup_type='contains',
    )
    chapter_cfi = django_filters.CharFilter(
        name='chapters__chapters_cfi',
        lookup_type='contains',
    )

    class Meta:
        model = AnnotationModel
        fields = ['chapter_cfi', 'book_name', 'book_id']


class AnnotationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnotationModel.objects.all()
    serializer_class = AnnotationSerializer
    filter_class = AnnotationFilter

def search(request):
    word = request.GET.get('q', None)
    book_id = request.GET.get('book_id', None)
    if not (word or book_id):
        return JsonResponse({'results': 'none'})
    book = BookModel.objects.get(pk=book_id)
    book_address = book.book_epub.file.name
    worker = EpubWorker(book_address)
    return JsonResponse(worker.search_word(word))