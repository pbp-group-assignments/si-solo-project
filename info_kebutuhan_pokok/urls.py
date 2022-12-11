from django.urls import path
from info_kebutuhan_pokok.views import show_kebutuhan_pokok, manage_kebutuhan_json, add_kebutuhan, delete_kebutuhan

app_name = 'info_kebutuhan_pokok'

urlpatterns = [
    path('', show_kebutuhan_pokok, name='show_kebutuhan_pokok'),
    path('manage-json/', manage_kebutuhan_json, name = "manage_kebutuhan_json"),
    path('add-kebutuhan', add_kebutuhan, name='add_kebutuhan'),
    path('delete-kebutuhan', delete_kebutuhan, name='delete_kebutuhan')
    
]