from rest_framework import serializers
from game_app.models import *


class OnGameUsersSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True)

    class Meta:
        model = OnGameUsers
        fields = ['user_name']


class ShopListSerializer(serializers.ModelSerializer):
    item_mame = serializers.CharField(required=True)
    item_cost = serializers.IntegerField()

    class Meta:
        model = ShopList
        fields = [' item_mame', 'item_cost ']


class ItemListSerializer(serializers.ModelSerializer):
    item_mame = serializers.CharField(required=True)
    item_cost = serializers.IntegerField()

    class Meta:
        model = ItemList
        fields = ['item_mame', 'item_cost ']

class RecordListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True)
    record = serializers.IntegerField(required=True)


    class Meta:
        model = RecordsList
        fields = ['user_name', 'record']


class HeroListSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset='auth.User')
    hero_name = serializers.CharField(max_length=200)

    class Meta:
        model = HeroesList
        fields = ['owner', 'hero_name']
