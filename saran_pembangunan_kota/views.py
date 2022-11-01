from ast import For
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from sisolo.models import User
from datetime import datetime
from django.core import serializers
from . import forms
from saran_pembangunan_kota.forms import FormSaran
from saran_pembangunan_kota.models import Saran
from django.shortcuts import redirect



# Create your views here.
@login_required(login_url='/login/')
@csrf_exempt
def show_saran(request):
    form = forms.FormSaran()
    if request.method == 'POST':
        form = FormSaran(request.POST)
        if form.is_valid():
            saran = FormSaran(
                        nama = form.cleaned_data['nama'],
                        email = form.cleaned_data['email'],
                        saran_pembangunan = form.cleaned_data['saran_pembangunan'],
            )
            saran.save()
            return redirect('saran_pembangunan_kota:show_saran')
    context = {'form': form}
    return render(request, 'form_saran.html', context)

@login_required(login_url='/login/')
def saran_json(request):
    daftar_saran = Saran.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", daftar_saran), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
def kirim_saran(request):
    form = forms.FormSaran()
    if request.method == 'POST':
        form = FormSaran(request.POST)
        if form.is_valid():
            saran = FormSaran(
                        nama = form.cleaned_data['nama'],
                        email = form.cleaned_data['email'],
                        saran_pembangunan = form.cleaned_data['saran_pembangunan'],
            )
            saran.save()
            return redirect('saran_pembangunan_kota:show_saran')
    context = {'form': form}
    return render(request, 'form_saran.html', context)