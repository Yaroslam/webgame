from rest_framework.generics import ListAPIView
from .serializers import *
import django_filters.rest_framework
from game_app.models import *
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class OnGameListApiView(viewsets.ModelViewSet):
    serializer_class = OnGameUsersSerializer
    queryset = OnGameUsers.objects.all()


class ShopListListApiView(viewsets.ModelViewSet):
    serializer_class = ShopListSerializer
    queryset = ShopList.objects.all()


class ItemListListApiView(viewsets.ModelViewSet):
    serializer_class = ItemListSerializer
    queryset = ItemList.objects.all()

    @action(methods=['GET'], detail=False)
    def get_stats(self, request, **kwargs):
        stats = ItemList.objects.values_list('item_stats', flat=True)
        return Response(stats)

    @action(methods=['DELETE'], detail=False)
    def delete_all_swords(self, request, **kwargs):
        swords = ItemList.objects.filter(Q(item_name__startswith="sword"))
        return Response(swords.delete())


class SingleItemListApiViewByGetParam(generics.ListAPIView):
    serializer_class = ItemListSerializer

    def get_queryset(self):
        queryset = ItemList.objects.all()
        item_name = self.request.query_params.get("item_name")
        if item_name is not None:
            queryset = queryset.filter(item_name=item_name)
        return queryset

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


class SearchHeroListApiView(generics.ListAPIView):
    queryset = HeroesList.objects.all()
    serializer_class = HeroListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['hero_name']