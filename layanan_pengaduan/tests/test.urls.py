from django.test import TestCase
from django.urls import reverse, resolve
from layanan_pengaduan.views import ajukan_pengaduan, pengaduan_json, show_pengaduan

class TestUrls(TestCase):
    def test_show_pengaduan(self):
        url = reverse('layanan_pengaduan:show_pengaduan')
        self.assertEquals(resolve(url).func, show_pengaduan)

    def test_show_pengaduan(self):
        url = reverse('layanan_pengaduan:pengaduan_json')
        self.assertEquals(resolve(url).func, pengaduan_json)

    def test_show_pengaduan(self):
        url = reverse('layanan_pengaduan:ajukan_pengaduan')
        self.assertEquals(resolve(url).func, ajukan_pengaduan)