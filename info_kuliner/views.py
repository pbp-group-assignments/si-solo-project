import json
from django.shortcuts import render
from info_kuliner.forms import TempatKulinerForms
from info_kuliner.models import TempatKuliner
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from sisolo.decorators import admin_only, allowed_users
from django.shortcuts import redirect

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def show_tempatkuliner(request):
    if is_ajax(request=request) : 
        p = TempatKuliner(kuliner_title='Test', kuliner_description='Berkeley', kuliner_highlight='Data baru', image_url='https://filestore.community.support.microsoft.com/api/images/371db990-f99c-49e3-a230-c7de0458f791?upload=true')
        p.save()
        context = TempatKuliner.objects.all().values()
        arr = []
        for i in context :
            arr += [i]
        return JsonResponse(arr, safe=False)
    else :
        return render(request, "tempat_kuliner.html", {})

def show_json(request):
    tempatkuliner_data = TempatKuliner.objects.all()
    return HttpResponse(serializers.serialize("json", tempatkuliner_data), content_type="application/json")

def show_json_by_id(request, id):
    tempatkuliner_data = TempatKuliner.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", tempatkuliner_data), content_type="application/json")