from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_show_saran_GET(self):
        response = self.client.get(reverse('saran_pembangunan_kota:show_saran'))
        self.assertEquals(response.status_code, 302)

    def test_saran_json_GET(self):
        response = self.client.get(reverse('saran_pembangungan_kota:saran_json'))
        self.assertEquals(response.status_code, 302)

    def kirim_saran_GET(self):
        response = self.client.get(reverse('saran_pembangunan_kota:kirim_saran'))
        self.assertEquals(response.status_code, 302)