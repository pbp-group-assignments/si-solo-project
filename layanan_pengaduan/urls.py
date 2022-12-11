from django.urls import path
from layanan_pengaduan.views import index, show_pengaduan, pengaduan_json

app_name = 'layanan_pengaduan'

urlpatterns = [
    path('', index, name='index'),
    path('pengaduan-json/', pengaduan_json, name='pengaduan_json'),
]