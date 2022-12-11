from django.urls import path
from info_sarana_kesehatan.views import show_healthcenter_info, show_json_healthcenter

app_name = 'info_sarana_kesehatan'

urlpatterns = [
    path('', show_healthcenter_info, name='show_healthcenter_info'),
    path('json/healthcenter/', show_json_healthcenter, name='show_json_healthcenter'),
]