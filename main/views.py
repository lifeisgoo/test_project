from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from main.models import BooksModel


class HomeView(ListView):
    template_name = 'main/index.html'
    # model = BooksModel
    # queryset = BooksModel.objects.all()
    def get_queryset(self):
        qs = BooksModel.objects.all()
        return qs


