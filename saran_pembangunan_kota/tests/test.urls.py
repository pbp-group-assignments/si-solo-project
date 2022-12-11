from django.test import TestCase
from django.urls import reverse, resolve
from saran_pembangunan_kota.views import show_saran, saran_json, kirim_saran

class TestUrls(TestCase):
    def test_show_pengaduan(self):
        url = reverse('sarab_pembangungan_kota:show_saran')
        self.assertEquals(resolve(url).func, show_saran)

    def test_show_pengaduan(self):
        url = reverse('saran_pembangunan_kota:saran_json')
        self.assertEquals(resolve(url).func, saran_json)

    def test_show_pengaduan(self):
        url = reverse('saran_pembangunan_kota:kirim_saran')
        self.assertEquals(resolve(url).func, kirim_saran)