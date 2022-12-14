from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from info_transportasi_umum.models import Transportation, Route, StopPoint

# Create your views here.

def show_transport_info(request):
    context = {
        'transportation': Transportation.objects.all()
    }

    return render(request, 'transportation_info.html', context)

# def search_transport(request):
#     if request.method == "POST":
#         search_keyword = request.POST.get('search_keyword')
#         show_json_transport(request)

#         return HttpResponse("Status code: 200")

#     return render(request, 'transportation_info.html', {})

def show_json_transport(request):
    data = Transportation.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_route(request, id):
    transport = Transportation.objects.get(pk=id)
    data = Route.objects.filter(transportation=transport)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_stop_point(request, id):
    route = Route.objects.get(pk=id)
    data = StopPoint.objects.filter(route=route)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")