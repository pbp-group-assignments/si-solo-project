from django.urls import path
from layanan_pengaduan.views import show_pengaduan, ajukan_pengaduan

app_name = 'layanan_pengaduan'

urlpatterns = [
    path('', show_pengaduan, name='show_pengaduan'),
    path('ajukan-pengaduan', ajukan_pengaduan, name='ajukan_pengaduan'),
]