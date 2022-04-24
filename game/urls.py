from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('game/', include('game_app.urls'), name='game'),
]

import execute
