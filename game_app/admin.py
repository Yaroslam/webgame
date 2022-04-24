from django.contrib import admin
from .resourses import *
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


@admin.register(ShopList)
class ShopListAdmin(ImportExportModelAdmin):
    list_display = ('item',)


@admin.register(ItemList)
class ItemListAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ('item_name', 'item_pic', 'item_cost', 'item_stats')
    history_list_display = ('item_name', 'item_pic', 'item_cost', 'item_stats')


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
