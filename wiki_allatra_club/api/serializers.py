from django.contrib.contenttypes.models import ContentType

from taggit.models import TaggedItem

from rest_framework import serializers

from wiki_allatra_club.reader.models import BookModel, ChapterBookModel
from wiki.plugins.annotations.models import AnnotationModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id','book_file_name','author')

class ChapterBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)
    class Meta:
        model = ChapterBookModel
        fields = ('chapter_cfi', 'book')

class TaggedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = ('tag', 'object_id')
class TagSerializer(serializers.Field):
    def to_representation(self, obj):
        if type(obj) is not list:
            annotation_type = ContentType.objects.get(app_label="annotations", model="annotationmodel")
            results = []
            for tag in obj.all():
                tags=TaggedItem.objects.filter(tag_id=tag.id)
                for tag in tags:
                    if tag.content_type == annotation_type:
                        annotation_obj = tag.content_object
                    else:
                        continue
                    urlpath = annotation_obj.article.urlpath_set.first()
                    result = {'title':annotation_obj.article.current_revision.title,
                      'content':annotation_obj.article.render(),
                      'url':urlpath.get_absolute_url()}
                    if result in results:
                        continue
                    results.append(result)
            return results
            # return [tag.name for tag in obj.all()]
        return obj

class ArticleSerializer(serializers.Field):
    def to_representation(self, annotation_obj):
        if type(annotation_obj) is not dict:
            return [str(tag) for tag in annotation_obj.tags.all()]


class AnnotationSerializer(serializers.Serializer):
    # tags = TaggedItemSerializer(many=True)
    # chapters = ChapterBookSerializer(many=True)
    # books = BookSerializer(many=True)
    # tags = TagSerializer(label='articles')
    # article = ArticleSerializer()

    # class Meta:
    #     model = AnnotationModel
    #     fields = ('id',  'article', 'tags')
    #
    # def to_representation(self, annotation_obj):
    #     if type(annotation_obj) is not dict:
    #         return [str(tag) for tag in annotation_obj.tags.all()]

    articles = serializers.SerializerMethodField()
    words = serializers.SerializerMethodField()

    def get_articles(self, obj):
        if type(obj) is not list:
            annotation_type = ContentType.objects.get(app_label="annotations", model="annotationmodel")
            results = []
            for tag in obj.tags.all():
                tags=TaggedItem.objects.filter(tag_id=tag.id)
                for tag in tags:
                    if tag.content_type == annotation_type:
                        annotation_obj = tag.content_object
                    else:
                        continue
                    urlpath = annotation_obj.article.urlpath_set.first()
                    result = {'title':annotation_obj.article.current_revision.title,
                      'content':annotation_obj.article.render(),
                      'url':urlpath.get_absolute_url()}
                    if result in results:
                        continue
                    results.append(result)
            return results
            # return [tag.name for tag in obj.all()]
        return obj

    def get_words(self, obj):
        return  [tag.name for tag in obj.tags.all()]

def split_and_remove_tags_from_content(content):
    content_formatted = content
    return content_formatted

# TODO: send all lexemes of word
# TODO: remove images and cut content to 300 symbols