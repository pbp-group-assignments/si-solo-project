from django.test import TestCase
from django.urls import reverse, resolve
from pendaftaran_izin_usaha.views import show_pendaftaran, usaha_json, daftar_usaha_baru, cancel, daftar_pelaku_usaha, ubah_group_pengguna

class TestUrls(TestCase):
    def test_show_pendaftaran(self):
        url = reverse('pendaftaran_izin_usaha:show_pendaftaran')
        self.assertEquals(resolve(url).func, show_pendaftaran)

    def test_show_pendaftaran(self):
        url = reverse('pendaftaran_izin_usaha:usaha_json')
        self.assertEquals(resolve(url).func, usaha_json)
    
    def test_show_pendaftaran(self):
        url = reverse('pendaftaran_izin_usaha:daftar_usaha_baru')
        self.assertEquals(resolve(url).func, daftar_usaha_baru)
    
    def test_show_pendaftaran(self):
        url = reverse('pendaftaran_izin_usaha:cancel')
        self.assertEquals(resolve(url).func, cancel)
    
    def test_show_pendaftaran(self):
        url = reverse('pendaftaran_izin_usaha:daftar_pelaku_usaha')
        self.assertEquals(resolve(url).func, daftar_pelaku_usaha)
    
    def test_show_pendaftaran(self):
        url = reverse('pendaftaran_izin_usaha:show_pendaftaran')
        self.assertEquals(resolve(url).func, ubah_group_pengguna)