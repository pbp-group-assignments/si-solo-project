from genericpath import exists
from queue import Empty
from tkinter import Menu
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pendaftaran_izin_usaha.models import Usaha
from sisolo.decorators import admin_only, allowed_users
from django.shortcuts import redirect
from info_kuliner.models import MenuKuliner

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def show_tempat_kuliner(request):
    return render(request, 'show_tempat_kuliner.html')

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def manage_kuliner_json(request):
    data = MenuKuliner.objects.filter(tempatKuliner = request.GET.get('id'))
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def add_menu_kuliner(request):
    if request.method == 'POST':
        idUsaha = request.POST.get('daftarId')
        tempatKuliner = Usaha.objects.get(pk = idUsaha)
        namaMenu = request.POST.get('namaMenu')
        hargaMenu = request.POST.get('hargaMenu')
        deskripsiMenu = request.POST.get('deskripsiMenu')
        menuKuliner = MenuKuliner(tempatKuliner = tempatKuliner, namaMenu = namaMenu, hargaMenu = hargaMenu, deskripsiMenu = deskripsiMenu)
        menuKuliner.save()

        response = {
            'pk':menuKuliner.pk,
            'fields':{
                'namaMenu':menuKuliner.namaMenu,
                'hargaMenu':menuKuliner.hargaMenu,
                'deskripsiMenu':menuKuliner.deskripsiMenu,
            }
        }

        return JsonResponse(response)

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def delete_menu_kuliner(request):
    if request.method == 'POST':
        idMenuString = request.POST.get('PKMenu')
        if (MenuKuliner.objects.filter(pk = idMenuString).exists()):
            MenuKuliner.objects.filter(pk = idMenuString).delete()
            response = {'status':'YES'}
        else:
            response = {'status':'NO'}
        return JsonResponse(response)