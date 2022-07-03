from rest_framework.generics import ListAPIView
from .serializers import *
import django_filters.rest_framework
from game_app.models import *
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User


class OnGameListApiView(viewsets.ModelViewSet):
    serializer_class = OnGameUsersSerializer
    queryset = OnGameUsers.objects.all()


class ShopListListApiView(viewsets.ModelViewSet):
    serializer_class = ShopListSerializer
    queryset = ShopList.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['item']

    @action(detail=False, methods=['POST'])
    def add_item(self, request, **kwargs):
        print(request.data['item'])
        item_to_add = int(request.data['item'])
        is_item_real = len(ItemList.objects.filter(id=item_to_add)) >= 1
        if is_item_real:
            shop = ShopList()
            shop.add_to_shop(ItemList.objects.filter(id=item_to_add)[0])
        else:
            return Response({"Response": "Item does not exist"})
        return Response({"Response": f"Item {item_to_add} added successfully"})


class ItemListListApiView(viewsets.ModelViewSet, generics.ListAPIView):
    serializer_class = ItemListSerializer
    queryset = ItemList.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['item_name']

    @action(methods=['GET'], detail=False)
    def get_stats(self, request, **kwargs):
        stats = ItemList.objects.values_list('item_stats', flat=True)
        return Response(stats)

    @action(methods=['POST'], detail=False)
    def delete_item_startwith(self, request, **kwargs):
        swords = ItemList.objects.filter(Q(item_name__startswith=request.POST['item_name']))
        return Response(swords.delete())


class SingleItemListApiViewByGetParam(generics.ListAPIView):
    serializer_class = ItemListSerializer

    def get_queryset(self):
        queryset = ItemList.objects.all()
        item_name = self.request.query_params.get("item_name", )
        if item_name is not None:
            queryset = queryset.filter(item_name=item_name)
        return queryset


class RecordsListApiView(viewsets.ModelViewSet):
    serializer_class = RecordListSerializer
    queryset = RecordsList.objects.all()

    @action(detail=False, methods=['POST'])
    def add_record(self, request, **kwargs):
        user_to_add = request.data['username']
        is_user_real = len(User.objects.filter(username=user_to_add)) >= 1
        if is_user_real:
            new_rec = RecordsList()
            new_rec.add_new_record(request.data['username'],  request.data['record'])
        else:
            return Response({"Response": "User does not exist"})
        return Response({"Response": f"Record of {user_to_add} added successfully"})


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

class  UsersListApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

