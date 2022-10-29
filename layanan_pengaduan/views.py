from ast import For
from django.shortcuts import render
from layanan_pengaduan.models import Pengaduan
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
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
def show_pengaduan(request):
    form = forms.FormPengaduan()
    if request.method == 'POST':
        form = FormPengaduan(request.POST)
        if form.is_valid():
            pengaduan_baru = FormPengaduan(
                                        judul_pengaduan = form.cleaned_data['judul_pengaduan'],
                                        deskripsi_pengaduan = form.cleaned_data['deskripsi_pengaduan']
            )
            pengaduan_baru.save()
            return redirect('layanan_pengaduan:show_pengaduan')
    context = {'form': form}
    return render(request, 'daftar_pengaduan.html', context)

@login_required(login_url='/login/')
def pengaduan_json(request):
    daftar_pengaduan = Pengaduan.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", daftar_pengaduan), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
def ajukan_pengaduan(request):
    form = forms.FormPengaduan()
    if request.method == 'POST':
        form = FormPengaduan(request.POST)
        if form.is_valid():
            pengaduan_baru = FormPengaduan(
                                        judul_pengaduan = form.cleaned_data['judul_pengaduan'],
                                        deskripsi_pengaduan = form.cleaned_data['deskripsi_pengaduan']
            )
            pengaduan_baru.save()
            return redirect('layanan_pengaduan:show_pengaduan')
    form = FormPengaduan()
    context = {'form': form}
    return render(request, 'daftar_pengaduan.html', context)