from django.urls import path
from .api_view import *
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Items', ItemListListApiView)
router.register(r'Shop', ShopListListApiView)
router.register(r'Records', RecordsListApiView)
router.register(r'OnGame', OnGameListApiView)
router.register(r'Heroes', AllHeroesListApiView)





urlpatterns = [path('', include(router.urls)),
               path('MyHeroes', LogUserHeroListApiView.as_view()),
               path('Item', SingleItemListApiViewByGetParam.as_view()),
               path('SearchHero', SearchHeroListApiView.as_view())
               ]
