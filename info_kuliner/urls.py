from unicodedata import name
from django.urls import path
from info_kuliner.views import manage_kuliner_json, add_menu_kuliner, delete_menu_kuliner, show_tempat_kuliner

app_name = 'info_kuliner'

urlpatterns = [
    path('', show_tempat_kuliner, name='show_tempat_kuliner'),
    path('manage-json/', manage_kuliner_json, name = "manage_kuliner_json"),
    path('add-menu-kuliner', add_menu_kuliner, name='add_menu_kuliner'),
    path('delete-menu-kuliner', delete_menu_kuliner, name='delete_menu_kuliner')
]