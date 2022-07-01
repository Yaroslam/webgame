from rest_framework import serializers
from game_app.models import *
from rest_framework.validators import UniqueValidator
from .validators import *
from django.contrib.auth.models import User


class OnGameUsersSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True, validators=[name_must_be_eng])

    class Meta:
        model = OnGameUsers
        fields = ['user_name']


class ShopListSerializer(serializers.ModelSerializer):
    item = serializers.CharField()

    class Meta:
        model = ShopList
        fields = ['item']


class ItemListSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=ItemList.objects.all()), name_must_be_eng])
    item_cost = serializers.IntegerField(validators=[must_be_int])
    item_stats = serializers.JSONField(validators=[not_null])

    class Meta:
        model = ItemList
        fields = ['id', 'item_name', 'item_cost', 'item_stats']


class RecordListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True, validators=[name_must_be_eng])
    record = serializers.IntegerField(required=True, validators=[must_be_int])


    class Meta:
        model = RecordsList
        fields = ['user_name', 'record']


class HeroListSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=True, validators=[name_must_be_eng])
    hero_name = serializers.CharField(max_length=200, validators=[name_must_be_eng])

    class Meta:
        model = HeroesList
        fields = ['owner', 'hero_name']

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'id']


