# blog/urls.py
from django.urls import path

from .views import (
    RecordView,
    GameView,
    ShopView,
    ItemDescriptionView,
    AccoutView
)

urlpatterns = [

    path('Account/', AccoutView.as_view(), name='account'),
    path('item/<int:pk>/', ItemDescriptionView.as_view(), name='item_detail'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('records/', RecordView.as_view(), name='records'),
    path('game/', GameView.as_view(), name='game'),
]