from rest_framework.generics import ListAPIView
from .serializers import *
from game_app.models import *
from rest_framework import viewsets, generics


class OnGameListApiView(viewsets.ModelViewSet):
    serializer_class = OnGameUsersSerializer
    queryset = OnGameUsers.objects.all()


class ShopListListApiView(viewsets.ModelViewSet):
    serializer_class = ShopListSerializer
    queryset = ShopList.objects.all()


class ItemListListApiView(viewsets.ModelViewSet):
    serializer_class = ItemListSerializer
    queryset = ItemList.objects.all()


class RecordsListApiView(viewsets.ModelViewSet):
    serializer_class = RecordListSerializer
    queryset = RecordsList.objects.all()


class AllHeroesListApiView(viewsets.ModelViewSet):
    serializer_class = HeroListSerializer
    queryset = HeroesList.objects.all()


class LogUserHeroListApiView(generics.ListAPIView):
    serializer_class = HeroListSerializer

    def get_queryset(self):
        user = self.request.user
        return HeroesList.objects.filter(owner=user)

