from django.urls import path
from Admin.views import show_admin_page, list_pendaftaran_json, list_pendaftaran_diajukan, get_detail_pendaftaran, set_diproses_pendaftaran
from Admin.views import list_pendaftaran_diproses, set_ditolak_pendaftaran, list_pendaftaran_ditolak, list_pendaftaran_diterima, set_diterima_pendaftaran
from Admin.views import add_berita

app_name = 'Admin'

urlpatterns = [
    path('', show_admin_page, name='show_admin_page'),
    path('list-pendaftaran-json', list_pendaftaran_json, name='list_pendaftaran_json'),
    path('list-pendaftaran',  list_pendaftaran_diajukan, name='list_pendaftaran_diajukan'),
    path('detail-pendaftaran/<permohonanId>', get_detail_pendaftaran, name='get_detail_pendaftaran'),
    path('set-diproses/<permohonanId>', set_diproses_pendaftaran, name='set_diproses_pendaftaran'),
    path('list-pendaftaran-diproses', list_pendaftaran_diproses, name='list_pendaftaran_diproses'),
    path('list-pendaftaran-ditolak', list_pendaftaran_ditolak, name='list_pendaftaran_ditolak'),
    path('list-pendaftaran-diterima', list_pendaftaran_diterima, name='list_pendaftaran_diterima'),
    path('set-ditolak/<permohonanId>', set_ditolak_pendaftaran, name='set_ditolak_pendaftaran'),
    path('set-diterima/<permohonanId>', set_diterima_pendaftaran, name='set_diterima_pendaftaran'),
    path('add-berita/', add_berita, name='add_berita'),
]