from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from info_transportasi_umum.models import Transportation, Route, StopPoint
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from sisolo.decorators import admin_only

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

@login_required(login_url='/sisolo/login/')
@admin_only
def add_transport(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.POST.get('image')
        transportation = Transportation(name=name, description=description, image=image)
        transportation.save()

        messages.success(request, 'A transportation mode has been added!')
        return redirect('info_transportasi_umum:show_transport_info')
    
    context = {}
    return render(request, 'add_transportation.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def add_route(request, id):
    if request.method == "POST":
        transportation = Transportation.objects.get(pk=id)
        from_to = request.POST.get('from_to')
        route = Route(transportation=transportation, from_to=from_to)
        route.save()

        messages.success(request, 'A route has been added!')
        return redirect('info_transportasi_umum:show_transport_info')
    
    context = {}
    return render(request, 'add_route.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def add_stop_point(request, id):
    if request.method == "POST":
        route = Route.objects.get(pk=id)
        stop_name = request.POST.get('stop_name')
        stop_location = request.POST.get('stop_location')
        stop_point = StopPoint(route=route, stop_name=stop_name, stop_location=stop_location)
        stop_point.save()

        messages.success(request, 'A stop point has been added!')
        return redirect('info_transportasi_umum:show_transport_info')
    
    context = {}
    return render(request, 'add_stop_point.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def delete_transport(request, id):
    task = Task.objects.get(pk=id)
    title = task.title
    task.delete()

    return HttpResponse("Task: " + title + " have been deleted")