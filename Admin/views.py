from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sisolo.decorators import admin_only
from pendaftaran_izin_usaha.models import Usaha, PelakuUsaha
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from sisolo.models import User
from Admin.forms import AlasanDitolak, NomorIzinUsaha
from django.views.decorators.csrf import csrf_exempt
from info_transportasi_umum.models import Transportation, Route, StopPoint
from info_transportasi_umum.forms import TransportationForm, RouteForm, StopPointForm, DeleteTransportationForm

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
    form = NomorIzinUsaha()
    return render(request, "list_pendaftaran_diproses.html", {'form':form})

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
        usaha = Usaha.objects.get(pk = permohonanId)
        usaha.statusPendaftaran = 'Ditolak'
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
def add_transport(request):
    if request.method == "POST":
        form = TransportationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Transportasi: " + form.cleaned_data['name'] + " berhasil ditambahkan!")
        else:
            return HttpResponse("Transportasi tidak berhasil ditambahkan!")
    
    context = {'form': TransportationForm()}
    return render(request, 'add_transportation.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def add_route(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Rute: " + form.cleaned_data['from_to'] + " berhasil ditambahkan!")
        else:
            return HttpResponse("Rute tidak berhasil ditambahkan!")
    
    context = {'form': RouteForm()}
    return render(request, 'add_route.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def add_stop_point(request):
    if request.method == "POST":
        form = StopPointForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Titik pemberhentian: " + form.cleaned_data['stop_name'] + " berhasil ditambahkan!")
        else:
            return HttpResponse("Titik pemberhentian tidak berhasil ditambahkan!")
    
    context = {'form': StopPointForm()}
    return render(request, 'add_stop_point.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def delete_transport(request):
    if request.method == "POST":
        form = DeleteTransportationForm(request.POST)
        if form.is_valid():
            transportation = form.cleaned_data['transportation']
            transport_name = transportation.name
            transportation.delete()
            return HttpResponse("Transportasi: " + transport_name + " berhasil dihapus!")
        else:
            return HttpResponse("Transportasi tidak berhasil dihapus!")
    
    context = {'form': DeleteTransportationForm()}
    return render(request, 'delete_transportation.html', context)

@login_required(login_url='/login/')
@admin_only
def pengaturan_info_transport(request):
    return render(request, "pengaturan_info_transport.html", {})