from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='root'),
    path('author/<int:author_id>/', views.author_about, name='author_about'), # Додайте цей рядок
]