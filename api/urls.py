from django.urls import path
from .api_view import *

urlpatterns = [path('OngameUsers/', OnGameListApiView.as_view(), name='onGame'),
               path('ShopList/', ShopListListApiView.as_view(), name='ShopList'),
               path('ItemList/', ItemListListApiView.as_view(), name='ItemList'),
               path('RecordList/', RecordsListApiView.as_view(), name='RecordList'),
               path('HeroesList/', HeroesListApiView.as_view(), name='HeroesList')]
