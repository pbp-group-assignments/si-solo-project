from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from info_transportasi_umum.models import Transportation, Route, StopPoint
from django.views.generic import DetailView

# Create your views here.

class ImageDisplay(DetailView):
    model = Transportation
    template_name = 'transportation_info.html'
    context_object_name = 'transport'

def show_transport_info(request):
    context = {
        'transportation': Transportation.objects.all()
    }

    return render(request, 'transportation_info.html', context)

def search_transport(request):
    if request.method == "GET":
        search_keyword = request.GET.get('search_keyword')
        context = {
        'transportation': Transportation.objects.filter(name__icontains=search_keyword)
        }

        return render(request, 'transportation_info.html', context)
    
    context = {
        'transportation': Transportation.objects.all()
    }

    return render(request, 'transportation_info.html', context)

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