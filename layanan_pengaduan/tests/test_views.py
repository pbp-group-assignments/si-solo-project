from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_show_pengaduan_GET(self):
        response = self.client.get(reverse('layanan_pengaduan:show_pengaduan'))
        self.assertEquals(response.status_code, 302)

    def test_pengaduan_json_GET(self):
        response = self.client.get(reverse('layanan_pengaduan:pengaduan_json'))
        self.assertEquals(response.status_code, 302)

    def ajukan_pengaduan_GET(self):
        response = self.client.get(reverse('layanan_pengaduan:ajukan_pengaduan'))
        self.assertEquals(response.status_code, 302)