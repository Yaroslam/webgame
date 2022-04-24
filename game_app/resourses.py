from import_export import resources
from .models import *

class ItemResourse(resources.ModelResource):

    class Meta:
        model = ItemList
        fields = ('item_name', 'item_cost', 'item_stats')
        export_order = ('item_name', 'item_cost', 'item_stats')
