from django.test import TestCase
from pendaftaran_izin_usaha.models import Usaha, PelakuUsaha
from sisolo.models import User

class TestModels(TestCase):
    def test_should_create_usaha(self):
        self.project1 = Usaha.objects.create(
            user = User object (12),
            namaPemilik = 'Rifqi Farel',
            nomorTeleponPemilik = '085892025984',
            alamatPemilik = 'Perumahan Grand Melati Residence Blok F11, Jalan Rawa Gede Raya, Kelurahan Jati Melati, Kecamatan Pondok Melati, Kota Bekasi',
            namaUsaha = 'Bakso Wenak',
            jenisUsaha = 'Kuliner',
            alamatUsaha = 'Bekasi',
            nomorTeleponUsaha = '451243234235435',
            statusPendaftara = 'Diproses'
        )

        testing = Usaha.objects.get(namaUsaha = 'Bakso Wenak')

        self.assertEquals(self.project1, testing)
    
    def test_should_create_usaha(self):
        self.project2 = Usaha.objects.create(
            user = User object (14),
            namaPemilik = 'cicak bin kadal',
            nomorTeleponPemilik = '2351432532',
            alamatPemilik = 'Bekasi',
            nik = '1234567891012132',
            status = 'Diterima'
        )

        testing = PelakuUsaha.objects.get(nik = '1234567891012132')

        self.assertEquals(self.project2, testing)