from django.shortcuts import render
from info_kuliner.models import TempatKuliner
from django.http import HttpResponse, JsonResponse
from django.core import serializers

def show_tempatkuliner(request):

    context = {
        'list_kuliner': TempatKuliner.objects.all(),
        'nama': " ",
    }
    return render(request, "tempatkuliner.html", context)

def show_json(request):
    tempatkuliner_data = TempatKuliner.objects.all()
    return HttpResponse(serializers.serialize("json", tempatkuliner_data), content_type="application/json")

def show_json_by_id(request, id):
    tempatkuliner_data = TempatKuliner.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", tempatkuliner_data), content_type="application/json")