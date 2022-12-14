from django.urls import path

from Admin.views import show_admin_page, list_pendaftaran_json, list_pendaftaran_diajukan, get_detail_pendaftaran, set_diproses_pendaftaran, show_list_kuliner_json, show_list_wisata_json
from Admin.views import list_pendaftaran_diproses, set_ditolak_pendaftaran, list_pendaftaran_ditolak, list_pendaftaran_diterima, set_diterima_pendaftaran
from Admin.views import add_kebutuhan, show_list_kebutuhan, set_ditolak_pendaftaran_mobile

from Admin.views import show_admin_page, list_pendaftaran_json, list_pendaftaran_diajukan, get_detail_pendaftaran, set_diproses_pendaftaran, show_list_wisata 
from Admin.views import list_pendaftaran_diproses, set_ditolak_pendaftaran, list_pendaftaran_ditolak, list_pendaftaran_diterima, set_diterima_pendaftaran
from Admin.views import add_kebutuhan, set_diterima_pendaftaran_mobile
from Admin.views import set_pengaduan_selesai, set_diterima_pelaku_usaha_mobile, set_diproses_pendaftaran_mobile

from Admin.views import  pendaftaran_pelaku_usaha_json, list_pendaftaran_pelaku_usaha_diproses, set_diterima_pelaku_usaha, list_pendaftaran_pelaku_usaha_diterima
from Admin.views import set_ditolak_pelaku_usaha, list_pendaftaran_pelaku_usaha_ditolak
from Admin.views import add_transport, add_route, add_stop_point, delete_transport, pengaturan_info_transport
from Admin.views import list_pengaduan_diproses, list_pengaduan_verifikasi, list_saran
from Admin.views import add_transport, add_route, add_stop_point, delete_transport, pengaturan_info_transport, show_list_kuliner, hapus_usaha
from Admin.views import add_healthcenter, delete_healthcenter, pengaturan_info_sarana_kesehatan, set_ditolak_pelaku_usaha_mobile

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
    path('add-kebutuhan/', add_kebutuhan, name='add_kebutuhan'),
    path('pendaftaran-pelaku-usaha-json', pendaftaran_pelaku_usaha_json, name='pendaftaran_pelaku_usaha_json'),
    path('pendaftaran-pelaku-usaha', list_pendaftaran_pelaku_usaha_diproses, name='list_pendaftaran_pelaku_usaha_diproses'),
    path('set-diterima-pelaku-usaha/<pkPemohon>', set_diterima_pelaku_usaha, name='set_diterima_pelaku_usaha'),
    path('list-pendaftaran-pelaku-usaha-diterima', list_pendaftaran_pelaku_usaha_diterima, name='list_pendaftaran_pelaku_usaha_diterima'),
    path('set-ditolak-pelaku-usaha/<pkPemohon>', set_ditolak_pelaku_usaha, name='set_ditolak_pelaku_usaha'),
    path('list-pendaftaran-pelaku-usaha-ditolak', list_pendaftaran_pelaku_usaha_ditolak, name='list_pendaftaran_pelaku_usaha_ditolak'),
    path('list-wisata-json/', show_list_wisata_json, name='show_list_wisata_json'),
    path('list-wisata/', show_list_wisata, name='show_list_wisata'),
    path('add-transport/', add_transport, name='add_transport'),
    path('add-route/', add_route, name='add_route'),
    path('add-stop-point/', add_stop_point, name='add_stop_point'),
    path('delete-transport/', delete_transport, name='delete_transport'),
    path('add-healthcenter/', add_healthcenter, name='add_healthcenter'),
    path('delete-transport/', delete_healthcenter, name='delete_healthcenter'),
    path('pengaturan-info-transport/', pengaturan_info_transport, name='pengaturan_info_transport'),
    path('pengaturan-info-sarana-kesehatan/', pengaturan_info_sarana_kesehatan, name='pengaturan_info_sarana_kesehatan'),
    path('list-pengaduan-diproses/', list_pengaduan_diproses, name='list_pengaduan_diproses'),
    path('list-pengaduan-verifikasi/', list_pengaduan_verifikasi, name='list_pengaduan_verifikasi'),
    path('list-saran/', list_saran, name='list_saran'),
    path('list-kuliner', show_list_kuliner, name='show_list_kuliner'),
    path('list-kuliner-json/', show_list_kuliner_json, name='show_list_kuliner_json'),
    path('hapus-usaha/<permohonanId>', hapus_usaha, name='hapus_usaha'),
    path('list-kebutuhan', show_list_kebutuhan, name='show_list_kebutuhan'),
    path('pengaduan-selesai/<permohonanId>', set_pengaduan_selesai, name='set_pengaduan_selesai'),
    path('set-diterima-pelaku-usaha-mobile', set_diterima_pelaku_usaha_mobile, name='set_diterima_pelaku_usaha_mobile'),
    path('set-ditolak-pelaku-usaha-mobile', set_ditolak_pelaku_usaha_mobile, name='set_ditolak_pelaku_usaha_mobile'),
    path('set-diproses-pendaftaran-mobile', set_diproses_pendaftaran_mobile, name='set_diproses_pendaftaran_mobile'),
    path('set-diterima-pendaftaran-mobile', set_diterima_pendaftaran_mobile, name='set_diterima_pendaftaran_mobile'),
    path('set-ditolak-pendaftaran-mobile', set_ditolak_pendaftaran_mobile, name='set_ditolak_pendaftaran_mobile'),
]