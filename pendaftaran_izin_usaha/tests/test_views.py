from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_show_pendaftaran_GET(self):
        response = self.client.get(reverse('pendaftaran_izin_usaha:show_pendaftaran'))
        self.assertEquals(response.status_code, 302)
    
    def test_usaha_json_GET(self):
        response = self.client.get(reverse('pendaftaran_izin_usaha:usaha_json'))
        self.assertEquals(response.status_code, 302)
    
    def test_daftar_usaha_baru_GET(self):
        response = self.client.get(reverse('pendaftaran_izin_usaha:daftar_usaha_baru'))
        self.assertEquals(response.status_code, 302)
    
    # def test_cancel_GET(self):
    #     response = self.client.get(reverse('pendaftaran_izin_usaha:cancel/1'))
    #     self.assertEquals(response.status_code, 302)

    def test_daftar_pelaku_usaha_GET(self):
        response = self.client.get(reverse('pendaftaran_izin_usaha:daftar_pelaku_usaha'))
        self.assertEquals(response.status_code, 302)
    
    def test_ubah_group_pengguna_GET(self):
        response = self.client.get(reverse('pendaftaran_izin_usaha:ubah_group_pengguna'))
        self.assertEquals(response.status_code, 302)