from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('newsletter.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('accounts/', include('allauth.urls')),
    path('ad_board/', include('ad_board.urls')),
    path('', include('newsletter.urls')),
    path('profile/', include('users.urls')),
    path('', include('chats.urls')),
    path('response_board/', include('response_board.urls')),
]
