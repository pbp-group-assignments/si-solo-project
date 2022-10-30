from django.contrib import admin
from info_transportasi_umum.models import Transportation, Route, StopPoint

# Register your models here.
admin.site.register(Transportation)
admin.site.register(Route)
admin.site.register(StopPoint)