from django.shortcuts import render
from pendaftaran_izin_usaha.models import Usaha, PelakuUsaha
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from sisolo.decorators import allowed_users
from sisolo.models import User
from django.shortcuts import redirect
from pendaftaran_izin_usaha.forms import DaftarPelakuUsaha, DaftarUsaha

# Create your views here.
@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha'])
def show_pendaftaran(request):
    form = DaftarUsaha()
    return render(request, "list_pendaftaran.html", {'form':form})

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Admin'])
def usaha_json(request):
    user = User.objects.get(user = request.user)
    data = Usaha.objects.filter(user = user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha'])
def daftar_usaha_baru(request):
    if request.method == 'POST':
        form = DaftarUsaha(request.POST)
        if form.is_valid():
            user = User.objects.get(user = request.user)
            namaUsaha = form.cleaned_data['namaUsaha']
            jenisUsaha = request.POST.get('jenisUsaha')
            alamatUsaha = form.cleaned_data['alamatUsaha']
            nomorTeleponUsaha = form.cleaned_data['nomorTeleponUsaha']
            usaha = Usaha(user = user, namaPemilik = user.namaLengkap, nomorTeleponPemilik = user.nomorTeleponPemilik, alamatPemilik = user.alamatPemilik, namaUsaha = namaUsaha, jenisUsaha = jenisUsaha, alamatUsaha = alamatUsaha, nomorTeleponUsaha = nomorTeleponUsaha)
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

    return HttpResponseBadRequest()

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha'])
def cancel(request, cancel_id):
    if (request.method == 'DELETE'):
        Usaha.objects.filter(id=cancel_id).delete()

        return HttpResponse(status=202)

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pengguna'])
def daftar_pelaku_usaha(request):
    user = User.objects.get(user = request.user)
    temp = PelakuUsaha.objects.filter(user = user)

    if not temp.exists():
        form = DaftarPelakuUsaha()

        if request.method == 'POST':
            form = DaftarPelakuUsaha(request.POST)
            if form.is_valid():
                user = User.objects.get(user = request.user)
                nik = request.POST.get('nik')
                pelakuUsaha = PelakuUsaha(user = user, namaPemilik = user.namaLengkap, nomorTeleponPemilik = user.nomorTeleponPemilik, alamatPemilik = user.alamatPemilik, nik = nik)
                pelakuUsaha.save()

                render(request, 'proses_pendaftaran_pelaku_usaha.html')
            
        context= {'form':form}
        return render(request, 'daftar_pelaku_usaha.html', context)
    else:
        pelakuUsaha = PelakuUsaha.objects.get(user = user)
        if pelakuUsaha.status == 'Diproses':
            return render(request, 'proses_pendaftaran_pelaku_usaha.html')
        elif pelakuUsaha.status == 'Ditolak':
            temp.delete()
            context={'pesan':pelakuUsaha.pesan}
            return render(request, 'tolak_pendaftaran_pelaku_usaha.html', context)
        else:
            return redirect('pendaftaran_izin_usaha:show_pendaftaran')

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pengguna'])
def ubah_group_pengguna(request):
    user = User.objects.get(user = request.user)
    user.role = 'Pelaku Usaha'
    user.save()
    return redirect('pendaftaran_izin_usaha:show_pendaftaran')