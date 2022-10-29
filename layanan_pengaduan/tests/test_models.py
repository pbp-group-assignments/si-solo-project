from django.test import TestCase
from layanan_pengaduan.models import Pengaduan
from sisolo.models import User

class TestModels(TestCase):
    def test_should_create_pengaduan(self):
        self.test1 = Pengaduan.objects.create(
            user = User.objects(10),
            judul_pengaduan = 'Lampu jalan mati',
            deskripsi_pengaduan = 'Tolong mas/mba diperbaiki, lampu jalan di perempatan keraton Solo mati, saya tadi hampir nabrak tukang becak',
            status_pengaduan = 'Diproses'
        )
        testing = Pengaduan.objects.get(namaUsaha = 'Bakso Wenak')
        self.assertEquals(self.project1, testing)