from django.contrib import admin
from .models import *
from import_export import resources



admin.site.register(Post)
admin.site.register(ShopList)
admin.site.register(ItemList)
admin.site.register(RecordsList)
admin.site.register(HeroesList)
admin.site.register(OnGameUsers)

class PersonResource(resources.ModelResource):
    class Meta:
        model = OnGameUsers


