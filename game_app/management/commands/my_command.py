from game_app.models import ShopList, ItemList
from random import randint
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        ShopList.objects.all().delete()
        Items = ItemList.objects.all()
        item_check = [1 for i in range(len(Items))]
        print(item_check)
        for i in range(6):
            random_item = randint(0, len(Items)-1)
            while item_check[random_item] == 0:
                random_item = randint(0, len(Items)-1)
            item = Items[random_item]
            item_check[random_item] = 0
            ShopList.objects.create(item=item)


