from django.urls import path
from pendaftaran_izin_usaha.views import show_pendaftaran, usaha_json, daftar_usaha_baru

app_name = 'pendaftaran_izin_usaha'

urlpatterns = [
    path('', show_pendaftaran, name='show_pendaftaran'),
    path('usaha-json/', usaha_json, name='usaha_json'),
    path('daftar-usaha-baru/', daftar_usaha_baru, name='daftar_usaha_baru'),
]