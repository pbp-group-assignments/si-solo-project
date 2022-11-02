from django.urls import path
from berita_isu_terkini.views import show_berita, manage_berita_json, add_berita, delete_berita

app_name = 'berita_isu_terkini'

urlpatterns = [
    path('', show_berita, name='show_berita'),
    path('manage-json/', manage_berita_json, name = "manage_berita_json"),
    path('add-berita', add_berita, name='add_berita'),
    path('delete-berita', delete_berita, name='delete_berita')
    
]