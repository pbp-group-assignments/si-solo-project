from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sisolo.decorators import admin_only
from pendaftaran_izin_usaha.models import Usaha
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from berita_isu_terkini.forms import Create
from django.shortcuts import redirect
from berita_isu_terkini.models import Berita

# Create your views here.
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
    return render(request, "list_pendaftaran_diproses.html", {})

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
@admin_only
def set_diproses_pendaftaran(request, permohonanId):
    if request.method == 'GET':
        usaha = Usaha.objects.get(pk = permohonanId)
        usaha.statusPendaftaran = 'Diproses'
        usaha.save()

        return HttpResponse(status=202)

@login_required(login_url='/login/')
@admin_only
def set_ditolak_pendaftaran(request, permohonanId):
    if request.method == 'GET':
        usaha = Usaha.objects.get(pk = permohonanId)
        usaha.statusPendaftaran = 'Ditolak'
        usaha.save()

        return HttpResponse(status=202)

@login_required(login_url='/login/')
@admin_only
def set_diterima_pendaftaran(request, permohonanId):
    if request.method == 'POST':
        usaha = Usaha.objects.get(pk = permohonanId)
        usaha.statusPendaftaran = 'Diterima'
        usaha.nomorIzinUsaha = request.POST.get('nomorIzinUsaha')
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
def add_berita(request):
    if request.method == "POST":
        news_title = request.POST.get('news_title')
        news_date = request.POST.get('news_date')
        news_image = request.POST.get('news_image')
        news_highlight = request.POST.get('news_highlight')
        berita = Berita(news_title=news_title, news_date=news_date, news_image=news_image, news_highlight=news_highlight)
        berita.save()

        return HttpResponse("Berita: " + news_title + " berhasil ditambahkan!")
    
    context = {}
    return render(request, 'add_news.html', context)

   