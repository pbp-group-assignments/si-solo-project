from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from sisolo.decorators import admin_only, allowed_users
from pendaftaran_izin_usaha.models import Usaha
# Create your views here.
from berita_isu_terkini.models import Berita
from sisolo.decorators import admin_only

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def show_berita(request):
    return render(request, 'beritaterkini.html')

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def manage_berita_json(request):
    data = Berita.objects.filter(penulisBerita = request.GET.get('id'))
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def add_berita(request):
    if request.method == 'POST':
        idUsaha = request.POST.get('daftarId')
        penulisBerita = Usaha.objects.get(pk = idUsaha)
        judulBerita = request.POST.get('judulBerita')
        highlightBerita = request.POST.get('highlightBerita')
        tanggalBerita = request.POST.get('tanggalBerita')
        berita = Berita(penulisBerita = penulisBerita, judulBerita = judulBerita, highlightBerita = highlightBerita, tanggalBerita = tanggalBerita)
        berita.save()

        response = {
            'pk':berita.pk,
            'fields':{
                'judulBerita':berita.judulBerita,
                'highlightBerita':berita.highlightBerita,
                'tanggalBerita':berita.tanggalBerita,
            }
        }

        return JsonResponse(response)

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def delete_berita(request):
    if request.method == 'POST':
        idBeritaString = request.POST.get('PKBerita')
        if (Berita.objects.filter(pk = idBeritaString).exists()):
            Berita.objects.filter(pk = idBeritaString).delete()
            response = {'status':'YES'}
        else:
            response = {'status':'NO'}
        return JsonResponse(response)
