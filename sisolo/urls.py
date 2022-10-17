from django.urls import path
from sisolo.views import landing_page, login_user, register, daftar_pelaku_usaha, ubah_group_pengguna

app_name = 'sisolo'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('daftar-pelaku-usaha/', daftar_pelaku_usaha, name='daftar_pelaku_usaha'),
    path('ubah-group-pengguna/', ubah_group_pengguna, name='ubah_group_pengguna')
]