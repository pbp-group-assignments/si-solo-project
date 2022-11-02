from django.test import TestCase
from saran_pembangunan_kota.models import Saran
from sisolo.models import User

class TestModels(TestCase):
    def test_should_create_pengaduan(self):
        self.test1 = Saran.objects.create(
            user = User.objects(10),
            nama = 'Mathilda Dellanova',
            email = 'mathilda.here@gmail.com',
            saran_pembangunan = 'Semoga jalur KRL diperbanyak supaya akses ke tempat-tempat wisata lebih mudah'
        )
        testing = Saran.objects.get(nama = 'Mathilda Dellanova')
        self.assertEquals(self.project1, testing)