from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from info_tempat_wisata.models import DaftarWisata
from pendaftaran_izin_usaha.models import Usaha
from sisolo.decorators import admin_only, allowed_users
from django.shortcuts import redirect

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def show_tempat_wisata(request):
    return render(request, 'show_tempat_wisata.html')

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def manage_wisata_json(request):
    data = DaftarWisata.objects.filter(tempatWisata = request.GET.get('id'))
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def add_deskripsi_wisata(request):
    if request.method == 'POST':
        idUsaha = request.POST.get('daftarId')
        tempatWisata = Usaha.objects.get(pk = idUsaha)
        namaWisata = request.POST.get('namaWisata')
        hargaWisata = request.POST.get('hargaWisata')
        deskripsiWisata = request.POST.get('deskripsiWisata')
        tempatWisata = DaftarWisata(tempatWisata = tempatWisata, namaWisata = namaWisata, hargaWisata = hargaWisata, deskripsiWisata = deskripsiWisata)
        tempatWisata.save()

        response = {
            'pk':tempatWisata.pk,
            'fields':{
                'namaWisata':tempatWisata.namaWisata,
                'hargaWisata':tempatWisata.hargaWisata,
                'deskripsiWisata':tempatWisata.deskripsiWisata,
            }
        }

        return JsonResponse(response)

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def delete_deskripsi_wisata(request):
    if request.method == 'POST':
        idMenuString = request.POST.get('PKWisata')
        if (DaftarWisata.objects.filter(pk = idMenuString).exists()):
            DaftarWisata.objects.filter(pk = idMenuString).delete()
            response = {'status':'YES'}
        else:
            response = {'status':'NO'}
        return JsonResponse(response)