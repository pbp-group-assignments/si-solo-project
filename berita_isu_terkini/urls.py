from django.urls import path
from berita_isu_terkini.views import show_berita, show_berita_json

app_name = 'berita_isu_terkini'

urlpatterns = [
    path('', show_berita, name='show_berita'),
    path('json/', show_berita_json, name='show_berita_json'),
    # path('add-berita/', show_create, name='show_create'),
]