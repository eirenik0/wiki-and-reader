from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import BookModel, AuthorModel

class ReaderView(DetailView):
    template_name = "pages/reader.html"
    model = BookModel
    context_object_name = 'book'
