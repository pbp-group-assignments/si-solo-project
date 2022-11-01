import json
from django.shortcuts import render
from info_tempat_wisata.forms import TempatWisataForms
from info_tempat_wisata.models import TempatWisata
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from sisolo.decorators import admin_only, allowed_users
from django.shortcuts import redirect

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def show_tempatwisata(request):
    if is_ajax(request=request) : 
        p = TempatWisata(wisata_title='Test', wisata_description='Berkeley', wisata_highlight='Data baru', image_url='https://filestore.community.support.microsoft.com/api/images/371db990-f99c-49e3-a230-c7de0458f791?upload=true')
        p.save()
        context = TempatWisata.objects.all().values()
        arr = []
        for i in context :
            arr += [i]
        return JsonResponse(arr, safe=False)
    else :
        return render(request, "tempat_wisata.html", {})
    

#    return render(request, "tempatwisata.html", context)

def show_json(request):
    tempatwisata_data = TempatWisata.objects.all()
    return HttpResponse(serializers.serialize("json", tempatwisata_data), content_type="application/json")

def show_json_by_id(request, id):
    tempatwisata_data = TempatWisata.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", tempatwisata_data), content_type="application/json")

@login_required(login_url='/sisolo/login/')
@csrf_exempt
@admin_only
def add_tempat_wisata(request):
    if request.user.is_authenticated:
        form = TempatWisataForms(request.POST)
        if request.method == 'POST' and form.is_valid():
            wisata_title = form.cleaned_data['title']
            wisata_description = form.cleaned_data['description']
            wisata_highlight = form.cleaned_data['highlight']
            wisata_image = request.POST.get('image')
            tempat_baru = TempatWisata.objects.create(title=wisata_title, description=wisata_description, highlight=wisata_highlight,
                                                image=wisata_image)
            return redirect('info_tempat_wisata:show_tempatwisata')
        
        context = {
            'form' : form,
        }
        return render(request, 'add_tempat_wisata.html', context)
    else:
        return HttpResponseBadRequest()

@login_required(login_url='/sisolo/login/')
@csrf_exempt
@admin_only
def tempat_wisata_baru(request):
    if request.method == 'POST':
        form = TempatWisataForms(request.POST)
        response_data = {}
        if form.is_valid():
            wisata_title = form.cleaned_data['title']
            wisata_description = form.cleaned_data['description']
            wisata_highlight = form.cleaned_data['highlight']
            response_data['title'] = wisata_title
            response_data['description'] = wisata_description
            response_data['highlight'] = wisata_highlight
            return JsonResponse(response_data);

        context = {
            'form': form,
        }
        return render(request, 'add_tempat_wisata.html', context)
    else:
        return HttpResponseBadRequest()

@login_required(login_url='/sisolo/login/')
@csrf_exempt
@admin_only
def delete_task(request, id):
    new_tempatwisata = TempatWisata.objects.get(id=id)
    new_tempatwisata.delete()
    return redirect('info_tempat_wisata:show_tempatwisata')

# @login_required(login_url='/login/')
# @csrf_exempt
# @allowed_users(allowed_roles=['Pelaku Usaha'])
# def daftar_wisata_baru(request):
#     if request.method == 'POST':
#         wisata_title = request.POST.get('wisata_title')
#         wisata_description = request.POST.get('wisata_description')
#         wisata_highlight = request.POST.get('wisata_highlight')
#         #( wisata_title = wisata_title, wisata_description = wisata_description, wisata_highlight = wisata_highlight)
#         usaha.save()

#         response = {
#             'pk':usaha.pk,
#             'fields':{
#                 'statusPendaftaran':usaha.statusPendaftaran,
#                 'namaUsaha':usaha.namaUsaha,
#                 'jenisUsaha':usaha.jenisUsaha,
#                 'alamatUsaha':usaha.alamatUsaha,
#                 'nomorTeleponUsaha':usaha.nomorTeleponUsaha,
#             }
#         }

#       return JsonResponse(response)