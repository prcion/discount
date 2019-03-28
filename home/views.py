from django.shortcuts import render
from django.http import HttpResponse
from .models import Discount
from django.views.generic import ListView, DetailView

class ShowNewsList(ListView):
    model = Discount
    template_name = "home/home.html"
    context_object_name = 'discount'
    ordering = ['-date']
    def get_context_data(self, **kwards):
        ctx = super(ShowNewsList, self).get_context_data(**kwards)
        ctx['title'] = 'Home'
        return ctx

class NewsDetailView(DetailView):
    model = Discount
    template_name = "home/discount_detail.html"
    context_object_name = 'post'
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = Discount.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
