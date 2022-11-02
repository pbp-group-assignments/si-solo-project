from ast import For
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from sisolo.decorators import allowed_users
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
def index(request):
    form = FormSaran()
    return render(request, "form_saran.html", {'form':form})

@login_required(login_url='/login/')
@csrf_exempt
def show_saran(request):
    form = forms.FormSaran()
    if request.method == 'POST':
        form = FormSaran(request.POST)
        if form.is_valid():
            user = User.objects.get(user = request.user)
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            saran_pembangunan = form.cleaned_data['saran_pembangunan']
            saran = Saran(user = user,
                            nama = nama,
                            email = email,
                            saran_pembangunan = saran_pembangunan
            )
            saran.save()
            response = {
                'pk':saran.pk,
                'fields':{
                    'nama':saran.nama,
                    'email':saran.email,
                    'saran_pembangunan':saran.saran_pembangunan,
                }
            }
            return JsonResponse(response)
    return HttpResponseBadRequest()

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Admin'])
def saran_json(request):
    user = User.objects.get(user = request.user)
    data = Saran.objects.filter(user = user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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