from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords
from random import randint



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hero = models.BooleanField(default=False)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class OnGameUsers(models.Model):
    user_name = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=200, default='play')

    def __str__(self):
        return self.user_name.username


class ShopList(models.Model):
    item = models.OneToOneField('ItemList', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.item.item_name

    def clear_shop(self):
        ShopList.objects.all().delete()

    def add_to_shop(self, item):
        new_item = ShopList()
        new_item.item = item
        new_item.save()



class ItemList(models.Model):
    item_name = models.CharField(max_length=200)
    item_pic = models.CharField(max_length=200)
    item_cost = models.IntegerField(max_length=200)
    item_stats = models.JSONField(default='')
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))

    def __str__(self):
        return self.item_name

    def random_item(self):
        count = ItemList.objects.all().count()
        random_index = randint(0, count - 1)
        return ItemList.objects.all()[random_index]


class RecordsList(models.Model):
    user_name = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    record = models.IntegerField()

    class Meta:
        ordering = ["-record"]

    def __str__(self):
        return self.user_name.username


class HeroesList(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    hero_name = models.CharField(max_length=200)
    hero_lvl = models.IntegerField(default=0)
    hero_stats = models.JSONField(default='')
    hero_inventory = models.JSONField(default='')
    hero_pic = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.hero_name

class LevelList(models.Model):
    level_name = models.TextField()
    level_dif = models.IntegerField()
