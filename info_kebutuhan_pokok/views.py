from django.shortcuts import render
from info_kebutuhan_pokok.models import KebutuhanPokok
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from pendaftaran_izin_usaha.models import Usaha
from sisolo.decorators import admin_only, allowed_users
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def show_kebutuhan_pokok(request):
    return render(request, 'show_kebutuhan_pokok.html')

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def manage_kebutuhan_json(request):
    data = KebutuhanPokok.objects.filter(tokoKebutuhan = request.GET.get('id'))
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def add_kebutuhan(request):
    if request.method == 'POST':
        idUsaha = request.POST.get('daftarId')
        tokoKebutuhan = Usaha.objects.get(pk = idUsaha)
        namaKebutuhan = request.POST.get('namaKebutuhan')
        hargaKebutuhan = request.POST.get('hargaKebutuhan')
        deskripsiKebutuhan = request.POST.get('deskripsiKebutuhan')
        kebutuhan = KebutuhanPokok(tokoKebutuhan = tokoKebutuhan, namaKebutuhan = namaKebutuhan, hargaKebutuhan = hargaKebutuhan, deskripsiKebutuhan = deskripsiKebutuhan)
        kebutuhan.save()

        response = {
            'pk':kebutuhan.pk,
            'fields':{
                'namaKebutuhan':kebutuhan.namaKebutuhan,
                'hargaKebutuhan':kebutuhan.hargaKebutuhan,
                'deskripsiKebutuhan':kebutuhan.deskripsiKebutuhan,
            }
        }

        return JsonResponse(response)

@login_required(login_url='/login/')
@csrf_exempt
@allowed_users(allowed_roles=['Pelaku Usaha', 'Pengguna'])
def delete_kebutuhan(request):
    if request.method == 'POST':
        idMenuString = request.POST.get('PKKebutuhan')
        if (KebutuhanPokok.objects.filter(pk = idMenuString).exists()):
            KebutuhanPokok.objects.filter(pk = idMenuString).delete()
            response = {'status':'YES'}
        else:
            response = {'status':'NO'}
        return JsonResponse(response)
# def show_kebutuhan(request):
#     if is_ajax(request=request) : 
#         p = Kebutuhan_Pokok(item='item', harga='harga', image='image')
#         p.save()
#         context = Kebutuhan_Pokok.objects.all().values()
#         arr = []
#         for i in context :
#             arr += [i]
#         return JsonResponse(arr, safe=False)
#     else :
#         return render(request, "kebutuhan.html", {})

# def show_kebutuhan_json(request):
#     data = Kebutuhan_Pokok.objects.all()
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'