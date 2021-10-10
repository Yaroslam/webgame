from django.db import models
from django.urls import reverse # Новый импорт

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])

class OnGameUsers(models.Model):
    user_name = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user_name.username

class ShopList(models.Model):
    item_mame = models.CharField(max_length=200)
    item_pic = models.CharField(max_length=200)
    item_cost = models.IntegerField()

    def __str__(self):
        return (self.item_mame, self.item_cost, self.item_pic)

class ItemList(models.Model):
    item_mame = models.CharField(max_length=200)
    item_pic = models.CharField(max_length=200)
    item_cost = models.IntegerField(max_length=200)

    def __str__(self):
        return self.item_mame

class RecordsList(models.Model):
    user_name = models.CharField(max_length=200)
    record = models.IntegerField()

    def __str__(self):
        return self.record

class HeroesList(models.Model):
    owner =models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    hero_name = models.CharField(max_length=200)

    def __str__(self):
        return self.hero_name
