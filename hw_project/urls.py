from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.register),
    path('', include('quotes.urls')),  # Головна сторінка з цитатами
    path('users/', include('users.urls')), # Сторінки реєстрації/логіну
]