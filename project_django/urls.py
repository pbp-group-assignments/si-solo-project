"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sisolo.urls')),
    path('daftar-usaha/', include('pendaftaran_izin_usaha.urls')),
    path('layanan-pengaduan/', include('layanan_pengaduan.urls')),
    path('saran-pembangunan-kota/', include('saran_pembangunan_kota.urls')),
    path('info-transportasi-umum/', include('info_transportasi_umum.urls')),
    path('Admin/', include('Admin.urls')),
    path('tempat-wisata/', include('info_tempat_wisata.urls')),
    path('tempat-kuliner/', include('info_kuliner.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)