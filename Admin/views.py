from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from info_tempat_wisata.forms import TempatWisataForms
from info_tempat_wisata.models import TempatWisata
from sisolo.decorators import admin_only
from pendaftaran_izin_usaha.models import Usaha, PelakuUsaha
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from sisolo.models import User
from Admin.forms import AlasanDitolak, NomorIzinUsaha
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login/')
@admin_only
def show_admin_page(request):
    context={}
    return render(request, 'Admin_page.html', context)

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_json(request):
    data = Usaha.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_diajukan(request):
    return render(request, "list_pendaftaran_diajukan.html", {})

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_diproses(request):
    form1 = NomorIzinUsaha()
    form2 = AlasanDitolak()
    return render(request, "list_pendaftaran_diproses.html", {'form1':form1, 'form2':form2})

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_ditolak(request):
    return render(request, "list_pendaftaran_ditolak.html", {})

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_diterima(request):
    return render(request, "list_pendaftaran_diterima.html", {})

@login_required(login_url='/login/')
@admin_only
def get_detail_pendaftaran(request, permohonanId):
    if request.method == 'GET':
        usaha = Usaha.objects.get(pk = permohonanId)
        response = {
            'pk': usaha.pk,
            'fields':{
                'namaPemilik':usaha.namaPemilik,
                'nomorTeleponPemilik':usaha.nomorTeleponPemilik,
                'alamatPemilik':usaha.alamatPemilik,
                'statusPendaftaran':usaha.statusPendaftaran,
                'namaUsaha':usaha.namaUsaha,
                'jenisUsaha':usaha.jenisUsaha,
                'alamatUsaha':usaha.alamatUsaha,
                'nomorTeleponUsaha':usaha.nomorTeleponUsaha,
                'nomorIzinUsaha':usaha.nomorIzinUsaha
            }
        }
        return JsonResponse(response)

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def set_diproses_pendaftaran(request, permohonanId):
    if request.method == 'POST':
        usaha = Usaha.objects.get(pk = permohonanId)
        usaha.statusPendaftaran = 'Diproses'
        usaha.save()

        return HttpResponse(status=202)

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def set_ditolak_pendaftaran(request, permohonanId):
    if request.method == 'POST':
        form = AlasanDitolak(request.POST)
        if form.is_valid():
            usaha = Usaha.objects.get(pk = permohonanId)
            alasan = form.cleaned_data['alasanDitolak']
            usaha.statusPendaftaran = 'Ditolak'
            usaha.alasanDitolak = alasan
            usaha.save()

            return HttpResponse(status=202)

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def set_diterima_pendaftaran(request, permohonanId):
    if request.method == 'POST':
        form = NomorIzinUsaha(request.POST)
        if form.is_valid():
            usaha = Usaha.objects.get(pk = permohonanId)
            usaha.statusPendaftaran = 'Diterima'
            usaha.nomorIzinUsaha = form.cleaned_data['nomorIzinUsaha']
            usaha.save()

            if (usaha.jenisUsaha == 'Kuliner'):
                print('Kuliner')
            elif (usaha.jenisUsaha == 'Tempat Wisata'):
                print('Tempat Wisata')
            else:
                print('Menjual Bahan Pokok')

            return HttpResponse(status=202)

@login_required(login_url='/login/')
@admin_only
def pendaftaran_pelaku_usaha_json(request):
    data = PelakuUsaha.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_pelaku_usaha_diproses(request):
    form = AlasanDitolak()
    return render(request, "list_pendaftaran_pelaku_usaha.html", {'form':form})

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_pelaku_usaha_diterima(request):
    return render(request, "list_pendaftaran_pelaku_usaha_diterima.html", {})

@login_required(login_url='/login/')
@admin_only
def list_pendaftaran_pelaku_usaha_ditolak(request):
    return render(request, "list_pendaftaran_pelaku_usaha_ditolak.html", {})

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def set_diterima_pelaku_usaha(request, pkPemohon):
    if request.method == 'POST':
        pelakuUsaha = PelakuUsaha.objects.get(pk = pkPemohon)
        pelakuUsaha.status = 'Diterima'
        pelakuUsaha.save()
        
        user = User.objects.get(user = pelakuUsaha.user.user)
        user.role = 'Pelaku Usaha'
        user.save()

        return HttpResponse(status=202)

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def set_ditolak_pelaku_usaha(request, pkPemohon):
    if request.method == 'POST':
        form = AlasanDitolak(request.POST)
        if form.is_valid():
            alasan = form.cleaned_data['alasanDitolak']
            pelakuUsaha = PelakuUsaha.objects.get(pk = pkPemohon)
            pelakuUsaha.status = 'Ditolak'
            pelakuUsaha.pesan = alasan
            pelakuUsaha.save()

            return HttpResponse(status=202)

@login_required(login_url='/sisolo/login/')
@admin_only
def tempat_wisata_baru(request):
    if request.method == 'POST':
        wisata_title = request.POST.get['wisata_title']
        wisata_description = request.POST.get['wisata_description']
        wisata_highlight = request.POST.get['wisata_highlight']
        wisata_image = request.POST.get['wisata_image']
        tempatwisata = TempatWisata(wisata_title=wisata_title, wisata_description=wisata_description, wisata_image=wisata_image, wisata_highlight=wisata_highlight)
        tempatwisata.save()
        return HttpResponse("Tempat wisata: " + wisata_title + " berhasil ditambahkan!")

    context = {}
    return render(request, 'add_tempat_wisata.html', context)

# @login_required(login_url='/sisolo/login/')
# @admin_only
# def delete_wisata(request, id):
#      if request.method == "POST":
#         ref_name = request.POST.get('ref_name')
#         tempatwisata = TempatWisata.objects.get(ref_name=ref_name)
#         tempatwisata.delete()

#         return HttpResponse("Transportasi: " + tempatwisata.name + " berhasil dihapus!")
    
#     context = {}
#     return render(request, 'delete_wisata.html', context)