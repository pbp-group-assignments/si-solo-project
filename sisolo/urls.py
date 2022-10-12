from django.urls import path
from sisolo.views import index

app_name = 'sisolo'

urlpatterns = [
    path('', index, name='index'),
]