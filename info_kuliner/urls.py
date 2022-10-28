from django.urls import path
from info_kuliner.views import show_tempatkuliner, show_json, show_json_by_id

app_name = 'info_kuliner'

urlpatterns = [
    path('', show_tempatkuliner, name = "show_tempatkuliner"),
    path('html/', show_tempatkuliner, name = "show_tempatkuliner"),
    path('json/', show_json, name = "show_json"),
    path('json/<int:id>/', show_json_by_id, name = "show_json_by_id"),
]