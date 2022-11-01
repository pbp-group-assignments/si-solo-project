from django.shortcuts import render
from info_kebutuhan_pokok.models import Kebutuhan_Pokok
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.

def show_kebutuhan(request):
    if is_ajax(request=request) : 
        p = Kebutuhan_Pokok(item='item', harga='harga', image='image')
        p.save()
        context = Kebutuhan_Pokok.objects.all().values()
        arr = []
        for i in context :
            arr += [i]
        return JsonResponse(arr, safe=False)
    else :
        return render(request, "kebutuhan.html", {})

def show_kebutuhan_json(request):
    data = Kebutuhan_Pokok.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'