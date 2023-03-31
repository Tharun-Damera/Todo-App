from django.urls import path

from .views import home_view, delete_view, clear_all

app_name = 'todo'

urlpatterns = [
    path('', home_view, name='home'),
    path('delete/<int:pk>', delete_view, name='delete'),
    path('clear_all/', clear_all, name='clear_all'),
]