from django.shortcuts import render
from pendaftaran_izin_usaha.models import Usaha
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from sisolo.decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha'])
def show_pendaftaran(request):
    context = {'username': request.user.get_username()}
    return render(request, "list_pendaftaran.html", context)

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha'])
def usaha_json(request):
    data = Usaha.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha'])
def daftar_usaha_baru(request):
    if request.method == 'POST':
        user = request.user
        namaPemilik = request.POST.get('namaPemilik')
        nomorTeleponPemilik = request.POST.get('nomorTeleponPemilik')
        alamatPemilik = request.POST.get('alamatPemilik')
        namaUsaha = request.POST.get('namaUsaha')
        jenisUsaha = request.POST.get('jenisUsaha')
        alamatUsaha = request.POST.get('alamatUsaha')
        nomorTeleponUsaha = request.POST.get('nomorTeleponUsaha')
        usaha = Usaha(user = user, namaPemilik = namaPemilik, nomorTeleponPemilik = nomorTeleponPemilik, alamatPemilik = alamatPemilik, namaUsaha = namaUsaha, jenisUsaha = jenisUsaha, alamatUsaha = alamatUsaha, nomorTeleponUsaha = nomorTeleponUsaha)
        usaha.save()

        response = {
            'pk':usaha.pk,
            'fields':{
                'statusPendaftaran':usaha.statusPendaftaran,
                'namaUsaha':usaha.namaUsaha,
                'jenisUsaha':usaha.jenisUsaha,
                'alamatUsaha':usaha.alamatUsaha,
                'nomorTeleponUsaha':usaha.nomorTeleponUsaha,
            }
        }

        return JsonResponse(response)