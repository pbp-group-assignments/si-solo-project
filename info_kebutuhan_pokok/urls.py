from django.urls import path
from info_kebutuhan_pokok.views import show_kebutuhan, show_kebutuhan_json

app_name = 'info_kebutuhan_pokok'

urlpatterns = [
    path('', show_kebutuhan, name='show_kebutuhan'),
    path('json/', show_kebutuhan_json, name='show_kebutuhan_json'),
    
]