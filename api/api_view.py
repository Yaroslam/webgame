from rest_framework.generics import ListAPIView
from .serializers import *
from game_app.models import *

class OnGameListApiView(ListAPIView):
    serializer_class = OnGameUsersSerializer
    queryset = OnGameUsers.objects.all()

class ShopListListApiView(ListAPIView):
    serializer_class = ShopListSerializer
    queryset = ShopList.objects.all()

class ItemListListApiView(ListAPIView):
    serializer_class = ItemListSerializer
    queryset = ItemList.objects.all()

class RecordsListApiView(ListAPIView):
    serializer_class = RecordListSerializer
    queryset = RecordsList.objects.all()

class HeroesListApiView(ListAPIView):
    serializer_class = HeroListSerializer
    queryset = HeroesList.objects.all()

