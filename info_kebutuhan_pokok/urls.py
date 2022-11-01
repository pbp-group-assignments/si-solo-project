from django.urls import path
from info_kebutuhan_pokok.views import show_kebutuhanpokok

app_name = 'kebutuhan_pokok'

urlpatterns = [
    path('', show_kebutuhanpokok, name= 'show_kebutuhanpokok'),
]