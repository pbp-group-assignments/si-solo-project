from django.contrib import admin
from pendaftaran_izin_usaha.models import Usaha, PelakuUsaha
from sisolo.models import User

# Register your models here.
admin.site.register(Usaha)
admin.site.register(User)
admin.site.register(PelakuUsaha)