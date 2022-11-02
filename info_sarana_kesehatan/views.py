from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from info_sarana_kesehatan.models import HealthCenter

# Create your views here.

def show_healthcenter_info(request):
    context = {
        'healthcenter': HealthCenter.objects.all()
    }

    return render(request, 'healthcenter_info.html', context)

def show_json_healthcenter(request):
    data = HealthCenter.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")