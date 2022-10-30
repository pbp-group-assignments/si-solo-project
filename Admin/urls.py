from django.urls import path
from Admin.views import show_admin_page, list_pendaftaran_json, list_pendaftaran_diajukan, get_detail_pendaftaran, set_diproses_pendaftaran
from Admin.views import list_pendaftaran_diproses, set_ditolak_pendaftaran, list_pendaftaran_ditolak, list_pendaftaran_diterima, set_diterima_pendaftaran
from Admin.views import  pendaftaran_pelaku_usaha_json, list_pendaftaran_pelaku_usaha_diproses, set_diterima_pelaku_usaha, list_pendaftaran_pelaku_usaha_diterima
from Admin.views import set_ditolak_pelaku_usaha, list_pendaftaran_pelaku_usaha_ditolak
from Admin.views import add_transport, add_route, add_stop_point, delete_transport, pengaturan_info_transport

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
    path('pendaftaran-pelaku-usaha-json', pendaftaran_pelaku_usaha_json, name='pendaftaran_pelaku_usaha_json'),
    path('pendaftaran-pelaku-usaha', list_pendaftaran_pelaku_usaha_diproses, name='list_pendaftaran_pelaku_usaha_diproses'),
    path('set-diterima-pelaku-usaha/<pkPemohon>', set_diterima_pelaku_usaha, name='set_diterima_pelaku_usaha'),
    path('list-pendaftaran-pelaku-usaha-diterima', list_pendaftaran_pelaku_usaha_diterima, name='list_pendaftaran_pelaku_usaha_diterima'),
    path('set-ditolak-pelaku-usaha/<pkPemohon>', set_ditolak_pelaku_usaha, name='set_ditolak_pelaku_usaha'),
    path('list-pendaftaran-pelaku-usaha-ditolak', list_pendaftaran_pelaku_usaha_ditolak, name='list_pendaftaran_pelaku_usaha_ditolak'),
    path('add-transport/', add_transport, name='add_transport'),
    path('add-route/', add_route, name='add_route'),
    path('add-stop-point/', add_stop_point, name='add_stop_point'),
    path('delete-transport/', delete_transport, name='delete_transport'),
    path('pengaturan-info-transport/', pengaturan_info_transport, name='pengaturan_info_transport'),
]