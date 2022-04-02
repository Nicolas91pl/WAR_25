from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from eshop.models import Product


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = [
        'name',
        'price',
        'description'
    ]
    success_url = reverse_lazy('list_product')


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        'name',
        'price',
        'description'
    ]
    success_url = reverse_lazy('list_product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list_product')
