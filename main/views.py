from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from main.forms import CreateBookForm
from main.models import BooksModel


class HomeView(ListView):
    template_name = 'main/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            qs = BooksModel.objects.all().filter(name__icontains=q)
        else:
            qs = BooksModel.objects.all()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            context['q'] = q

        return context


class CreateBookView(CreateView):
    model = BooksModel
    template_name = 'main/form.html'
    fields = ['name', 'price']
    success_url = '/'


class UpdateBookView(UpdateView):
    model = BooksModel
    template_name = 'main/update.html'
    fields = ['name', 'price']
    success_url = '/'


class BookDeteailView(DetailView):
    model = BooksModel
    template_name = 'main/detail.html'


class BookDeleteView(DeleteView):
    model = BooksModel

    def get_success_url(self):
        return reverse('home')

class MainView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')

        if q:
            qs = BooksModel.objects.all().filter(name__icontains=q)
        else:
            qs = BooksModel.objects.all()

        return render(request, 'main/index.html', context={
            'books': qs,
            'form': CreateBookForm
        })

    def post(self, request, *args, **kwargs):
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')