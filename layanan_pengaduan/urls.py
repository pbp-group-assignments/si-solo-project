from django.urls import path
from layanan_pengaduan.views import show_pengaduan, ajukan_pengaduan, pengaduan_json

app_name = 'layanan_pengaduan'

urlpatterns = [
    path('', show_pengaduan, name='show_pengaduan'),
    path('ajukan-pengaduan', ajukan_pengaduan, name='ajukan_pengaduan'),
    path('pengaduan-json/', pengaduan_json, name='pengaduan_json'),
]