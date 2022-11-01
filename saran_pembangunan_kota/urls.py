from django.urls import path
from saran_pembangunan_kota.views import show_saran, kirim_saran, saran_json

app_name = 'saran_pembangunan_kota'

urlpatterns = [
    path('', show_saran, name='show_saran'),
    path('kirim-saran/', kirim_saran, name='kirim_saran'),
    path('saran-json/', saran_json, name='saran_json'),
]