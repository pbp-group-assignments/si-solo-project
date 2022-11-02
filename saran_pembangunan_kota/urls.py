from django.urls import path
from saran_pembangunan_kota.views import index, saran_json

app_name = 'saran_pembangunan_kota'

urlpatterns = [
    path('', index, name='index'),
    path('saran-json/', saran_json, name='saran_json'),
]