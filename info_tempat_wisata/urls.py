from django.urls import path
from info_tempat_wisata.views import *

app_name = 'info_tempat_wisata'

urlpatterns = [
    path('', show_tempatwisata, name = "show_tempatwisata"),
    path('json/', show_json, name = "show_json"),
    path('json/<int:id>/', show_json_by_id, name = "show_json_by_id"),
]
