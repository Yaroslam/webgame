from game_app.models import ShopList, ItemList


def fill_shop_arr():
    i = 0
    items = []
    item_list = ItemList()
    while i != 10:
        new_item = item_list.random_item()
        if new_item not in items:
            items.append(new_item)
            i += 1
    return items


def refill_shop():
    shop = ShopList()
    shop.clear_shop()
    items = fill_shop_arr()
    for i in items:
        shop.add_to_shop(i)
    is_item_real = len(ItemList.objects.filter(id=13)) >= 1
    print(is_item_real)
    print(ItemList.objects.filter(id=13)[0])
    print("i fiil")

