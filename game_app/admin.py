from django.contrib import admin
from .resourses import *
from import_export.admin import ImportExportModelAdmin


#TODO:
#   1)сделать регистарцию
#   2)переписать логику таблиц
#       2.1)в айтемы добавить статы
#       2.2)придумать что то с персонажами
#       2.3) переписать юзер
#   3)дбавить мин функционал сайту
#
@admin.register(ShopList)
class ShopListAdmin(ImportExportModelAdmin):
    list_display = ('item',)

@admin.register(ItemList)
class ItemListAdmin(ImportExportModelAdmin):
    list_display = ('item_mame', 'item_pic', 'item_cost', 'item_stats')

@admin.register(RecordsList)
class RecordsAdmin(ImportExportModelAdmin):
    list_display = ('user_name', 'record')

@admin.register(HeroesList)
class HeroesListAdmin(admin.ModelAdmin):
    list_display = ('owner', 'hero_name')
    list_filter = ['owner']

@admin.register(OnGameUsers)
class OnGameUsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'status')
    list_filter = ['status']

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'is_hero')





