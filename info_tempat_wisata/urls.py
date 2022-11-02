from django.urls import path
from info_tempat_wisata.views import *

app_name = 'info_tempat_wisata'

urlpatterns = [
    path('', show_tempat_wisata, name = "show_tempat_wisata"),
    path('manage-json/', manage_wisata_json, name = "manage_wisata_json"),
    path('add-deskripsi-wisata', add_deskripsi_wisata, name='add_deskripsi_wisata'),
    path('delete-deskripsi-wisata', delete_deskripsi_wisata, name='delete_deskripsi_wisata')
]
