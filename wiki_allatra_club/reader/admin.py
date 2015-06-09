from django.contrib import admin
from .models import BookModel, AuthorModel, ChapterBookModel, async_add_chapters_to_book
from django.utils.translation import ugettext_lazy as _


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'is_chapters_connected_to_book')
    actions = ['add_chapters_to_book']

    def add_chapters_to_book(self, request, queryset):
        just_connected = []
        already_connected = []
        for instance in queryset:
            if not instance.chapterbookmodel_set.all():
                result = async_add_chapters_to_book.delay(instance)
                if result:
                    just_connected.append(instance.title)
            else:
                already_connected.append(instance.title)
        if already_connected and just_connected:
            result_message = _("Next books were already connected {}. This book were just connected {}".format(', '.join(already_connected),                                                                                                           ', '.join(just_connected)))
        elif just_connected and not already_connected:
            result_message = _("Books {} were just connected".format(', '.join(just_connected)))
        elif already_connected:
            result_message = _("Books {} already connected".format(', '.join(already_connected)))
        else:
            result_message = _("Something was going wrong")

        self.message_user(request, result_message)
    add_chapters_to_book.short_description = _("Add chapters to book")

admin.site.register(AuthorModel)
admin.site.register(ChapterBookModel)
admin.site.register(BookModel, BookAdmin)
