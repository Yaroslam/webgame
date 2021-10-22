# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # новое
from django.urls import reverse_lazy  # импортируем новые методы

from .models import *

class RecordView(ListView):
    model = RecordsList
    template_name = 'recordTable.html'

class GameView(ListView):
    model = Profile
    template_name = 'home.html'

class ShopView(ListView):
    model = ShopList
    template_name = 'shop.html'

class ItemDescriptionView(DetailView):
    model = ItemList
    template_name = 'ItemDescription.html'

class AccoutView(ListView):
    model = HeroesList
    template_name = 'Account.html'

    @staticmethod
    def Heroes():
        return HeroesList.objects.all()

    @staticmethod
    def Profiles():
        return Profile.objects.all()
