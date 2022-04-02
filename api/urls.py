from django.urls import path
from .api_view import *
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Items', ItemListListApiView)
router.register(r'OnGme', OnGameListApiView)
router.register(r'Shop', ShopListListApiView)
router.register(r'Records', RecordsListApiView)
router.register(r'Heroes', HeroesListApiView)





urlpatterns = [url(r'^', include(router.urls)),]
