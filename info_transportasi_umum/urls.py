from django.urls import path
from info_transportasi_umum.views import show_transport_info, show_json_transport, show_json_route, show_json_stop_point

app_name = 'info_transportasi_umum'

urlpatterns = [
    path('', show_transport_info, name='show_transport_info'),
    path('json/transportation/', show_json_transport, name='show_json_transport'),
    path('json/route/<int:id>/', show_json_route, name='show_json_route'),
    path('json/stop-point/<int:id>/', show_json_stop_point, name='show_json_stop_point'),
]