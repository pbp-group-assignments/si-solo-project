from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from info_kebutuhan_pokok.models import KebutuhanPokok

from sisolo.decorators import admin_only
from pendaftaran_izin_usaha.models import Usaha, PelakuUsaha
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import datetime
from django.shortcuts import redirect
from sisolo.models import User
from Admin.forms import AlasanDitolak, NomorIzinUsaha
from django.views.decorators.csrf import csrf_exempt
from info_transportasi_umum.forms import TransportationForm, RouteForm, StopPointForm, DeleteTransportationForm
from layanan_pengaduan.models import Pengaduan
from info_transportasi_umum.forms import TransportationForm, RouteForm, StopPointForm, DeleteTransportationForm
from info_sarana_kesehatan.forms import HealthCenterForm, DeleteHealthCenterForm

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
            return HttpResponse(status=202)

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def hapus_usaha(request, permohonanId):  #Semuanya pake ini kalau mau hapus usaha
    if request.method == 'POST':
        usaha = Usaha.objects.get(pk = permohonanId)
        usaha.delete()
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
def show_list_wisata(request):  #Untuk nampilin data wisata
    context = {}
    return render(request, 'list_wisata.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def show_list_kuliner(request):  #Untuk nampilin data kuliner
    context = {}
    return render(request, 'list_kuliner.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only

def show_list_kebutuhan(request):  
    context = {}
    return render(request, 'list_kebutuhan.html', context)
   

def add_transport(request):
    if request.method == "POST":
        form = TransportationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['last_activity'] = "add transportation"
            return HttpResponse("Transportasi: " + form.cleaned_data['name'] + " berhasil ditambahkan!")
        else:
            return HttpResponse("Transportasi tidak berhasil ditambahkan!")
    
    context = {'form': TransportationForm()}
    return render(request, 'add_transportation.html', context)



@login_required(login_url='/login/')
@admin_only
def add_kebutuhan(request):
    if request.method == "POST":
        namaKebutuhan = request.POST.get('namaKebutuhan')
        hargaKebutuhan = request.POST.get('hargaKebutuhan')
        deskripsiKebutuhan = request.POST.get('deskripsiKebutuhan')
       
        kebutuhan = KebutuhanPokok(namaKebutuhan=namaKebutuhan, hargaKebutuhan=hargaKebutuhan, deskripsiKebutuhan=deskripsiKebutuhan)
        kebutuhan.save()

        return HttpResponse("Item: " + namaKebutuhan + " berhasil ditambahkan!")
    
    context = {}
    return render(request, 'add_kebutuhan.html', context)


   
@login_required(login_url='/sisolo/login/')
@admin_only
def add_route(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['last_activity'] = "add route"
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
            request.session['last_activity'] = "add stop point"
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
            request.session['last_activity'] = "delete transportation"
            return HttpResponse("Transportasi: " + transport_name + " berhasil dihapus!")
        else:
            return HttpResponse("Transportasi tidak berhasil dihapus!")
    
    context = {'form': DeleteTransportationForm()}
    return render(request, 'delete_transportation.html', context)

@login_required(login_url='/login/')
@admin_only
def pengaturan_info_transport(request):
    context = {'last_activity': request.session.get('last_activity', "")}
    return render(request, "pengaturan_info_transport.html", context)

@login_required(login_url='/sisolo/login/')
@admin_only
def add_healthcenter(request):
    if request.method == "POST":
        form = HealthCenterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['last_activity'] = "add health center"
            return HttpResponse("Tempat layanan kesehatan: " + form.cleaned_data['name'] + " berhasil ditambahkan!")
        else:
            return HttpResponse("Tempat layanan kesehatan tidak berhasil ditambahkan!")
    
    context = {'form': HealthCenterForm()}
    return render(request, 'add_healthcenter.html', context)

@login_required(login_url='/sisolo/login/')
@admin_only
def delete_healthcenter(request):
    if request.method == "POST":
        form = DeleteHealthCenterForm(request.POST)
        if form.is_valid():
            healthcenter = form.cleaned_data['healthcenter']
            healthcenter_name = healthcenter.name
            healthcenter.delete()
            request.session['last_activity'] = "delete transportation"
            return HttpResponse("Tempat layanan kesehatan: " + healthcenter_name + " berhasil dihapus!")
        else:
            return HttpResponse("Tempat layanan kesehatan tidak berhasil dihapus!")
    
    context = {'form': DeleteTransportationForm()}
    return render(request, 'delete_transportation.html', context)

@login_required(login_url='/login/')
@admin_only
def pengaturan_info_sarana_kesehatan(request):
    context = {'last_activity': request.session.get('last_activity', "")}
    return render(request, "pengaturan_info_sarana_kesehatan.html", context)

@login_required(login_url='/login/')
@admin_only
def list_pengaduan_diproses(request):
    return render(request, "list_pengaduan_diproses.html", {})

@login_required(login_url='/login/')
@admin_only
def list_pengaduan_verifikasi(request):
    return render(request, "list_pengaduan_verifikasi.html", {})

@login_required(login_url='/login/')
@admin_only
def list_saran(request):
    return render(request, "list_saran.html", {})

@login_required(login_url='/login/')
@admin_only
def list_pengaduan_diproses(request):
    return render(request, "list_pengaduan_diproses.html", {})

@login_required(login_url='/login/')
@admin_only
def list_pengaduan_verifikasi(request):
    return render(request, "list_pengaduan_verifikasi.html", {})

@login_required(login_url='/login/')
@admin_only
def list_saran(request):
    return render(request, "list_saran.html", {})

@login_required(login_url='/login/')
@csrf_exempt
@admin_only
def set_pengaduan_selesai(request, permohonanId):
    if request.method == 'POST':
        pengaduan = Pengaduan.objects.get(pk = permohonanId)
        pengaduan.status_pengaduan = True
        pengaduan.save()

        return HttpResponse(status=202)