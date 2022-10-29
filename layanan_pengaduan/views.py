from django.shortcuts import render
from layanan_pengaduan.models import Pengaduan
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from sisolo.models import User
from datetime import datetime
from django.core import serializers

# Create your views here.
@login_required(login_url='/login/')
@csrf_exempt
def show_pengaduan(request):
    form_pengaduan = Pengaduan()
    return render(request, "daftar_pengaduan.html", {'form':form_pengaduan})

@login_required(login_url='/login/')
def pengaduan_json(request):
    user = User.objects.get(user = request.user)
    data = Pengaduan.objects.filter(user = user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
def ajukan_pengaduan(request):
    if request.method == 'POST':
        form = Pengaduan(request.POST)
        if form.is_valid():
            user = User.objects.get(user = request.user)
            tanggal_pengaduan = datetime.now()
            judul_pengaduan = form.cleaned_data['judul_pengaduan']
            deskripsi_pengaduan = form.cleaned_data['deskripsi']
            status_pengaduan = False
            pengaduan = Pengaduan(user = user, 
                                    tanggal_pengaduan = tanggal_pengaduan,
                                    judul_pengaduan = judul_pengaduan, 
                                    deskripsi_pengaduan = deskripsi_pengaduan,
                                    status_pengaduan = status_pengaduan)
            pengaduan.save()

            response = {
                'pk':pengaduan.pk,
                'fields':{
                    'tanggal_pengaduan':pengaduan.tanggal_pengaduan,
                    'judul_pengaduan':pengaduan.judul_pengaduan,
                    'deskripsi_pengaduan':pengaduan.deskripsi_pengaduan,
                    'status_pengaduan':pengaduan.status_pengaduan,
                }
            }
            return JsonResponse(response)
    return HttpResponseBadRequest()