from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('', include('game_app.urls')),
]