from django.urls import path
from pendaftaran_izin_usaha.views import show_pendaftaran, usaha_json, daftar_usaha_baru, cancel, daftar_pelaku_usaha, ubah_group_pengguna, proses_daftar_pelaku_usaha, daftar_ulang, semua_usaha_json, daftar_pelaku_usaha_mobile, get_usaha_mobile, add_pelaku_usaha, daftar_ulang_mobile, usaha_json_mobile, add_usaha_mobile

app_name = 'pendaftaran_izin_usaha'

urlpatterns = [
    path('', show_pendaftaran, name='show_pendaftaran'),
    path('usaha-json/', usaha_json, name='usaha_json'),
    path('daftar-usaha-baru/', daftar_usaha_baru, name='daftar_usaha_baru'),
    path('cancel/<cancel_id>', cancel, name='cancel'),
    path('daftar-pelaku-usaha/', daftar_pelaku_usaha, name='daftar_pelaku_usaha'),
    path('ubah-group-pengguna/', ubah_group_pengguna, name='ubah_group_pengguna'),
    path('proses-daftar-pelaku-usaha', proses_daftar_pelaku_usaha, name='proses_daftar_pelaku_usaha'),
    path('daftar-ulang', daftar_ulang, name='daftar_ulang'),
    path('semua-usaha-json', semua_usaha_json, name='semua_usaha_json'),
    path('daftar-pelaku-usaha-mobile/<role>/<namaLengkap>/<nomorTeleponPemilik>/<alamatPemilik>', daftar_pelaku_usaha_mobile, name='daftar_pelaku_usaha_mobile'),
    path('get-usaha-mobile/<role>/<namaLengkap>/<nomorTeleponPemilik>/<alamatPemilik>', get_usaha_mobile, name='get_usaha_mobile'),
    path('add-pelaku-usaha/', add_pelaku_usaha, name='add_pelaku_usaha'),
    path('daftar-ulang-mobile/', daftar_ulang_mobile, name='daftar_ulang_mobile'),
    path('add-usaha-mobile/', add_usaha_mobile, name='add_usaha_mobile'),
    path('usaha-json-mobile/<role>/<namaLengkap>/<nomorTeleponPemilik>/<alamatPemilik>', usaha_json_mobile, name='usaha_json_mobile'),
]