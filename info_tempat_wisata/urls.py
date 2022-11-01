from django.urls import path
from info_tempat_wisata.views import *

app_name = 'info_tempat_wisata'

urlpatterns = [
    path('', show_tempatwisata, name = "show_tempatwisata"),
    path('json/', show_json, name = "show_json"),
    path('json/<int:id>/', show_json_by_id, name = "show_json_by_id"),
    path('create-wisata/', add_tempat_wisata, name='add_tempat_wisata'),
    path('add-tempat-wisata/', tempat_wisata_baru, name="tempat_wisata_baru" ),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]
