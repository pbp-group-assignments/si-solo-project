from ast import For
from django.shortcuts import render
from layanan_pengaduan.models import Pengaduan
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from sisolo.decorators import admin_only
from sisolo.models import User
from datetime import datetime
from django.core import serializers
from . import forms
from layanan_pengaduan.forms import FormPengaduan
from django.shortcuts import redirect

import layanan_pengaduan


# Create your views here.
@login_required(login_url='/login/')
@csrf_exempt
def index(request):
    form = FormPengaduan()
    return render(request, "daftar_pengaduan.html", {'form':form})

@login_required(login_url='/login/')
@csrf_exempt
def show_pengaduan(request):
    form = forms.FormPengaduan()
    if request.method == 'POST':
        form = FormPengaduan(request.POST)
        if form.is_valid():
            user = User.objects.get(user = request.user)
            tanggal_pengaduan = datetime.date.today()
            judul_pengaduan = form.cleaned_data['judul_pengaduan']
            deskripsi_pengaduan = form.cleaned_data['deskripsi_pengaduan']
            status_pengaduan = False
            pengaduan_baru = Pengaduan(user = user,
                                            tanggal_pengaduan = tanggal_pengaduan,
                                            judul_pengaduan = judul_pengaduan,
                                            deskripsi_pengaduan = deskripsi_pengaduan,
                                            status_pengaduan = status_pengaduan
            )
            pengaduan_baru.save()
            response = {
                'pk':pengaduan_baru.pk,
                'fields':{
                    'tanggal_pengaduan':pengaduan_baru.tanggal_pengaduan,
                    'judul_pengaduan':pengaduan_baru.judul_pengaduan,
                    'deskripsi_pengaduan':pengaduan_baru.deskripsi_pengaduan,
                    'status_pengaduan':pengaduan_baru.status_pengaduan,
                }
            }
            return JsonResponse(response)
    return HttpResponseBadRequest()

@login_required(login_url='/login/')
@admin_only
def pengaduan_json(request):
    data = Pengaduan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")