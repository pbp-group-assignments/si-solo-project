from django.urls import path, include
from sisolo.views import landing_page, login_user, register, registerAddition, logout_user
import info_tempat_wisata.urls as urltempatwisata

app_name = 'sisolo'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('registerAddition/', registerAddition, name='registerAddition'),
    path('tempat-wisata/', include(urltempatwisata))
]