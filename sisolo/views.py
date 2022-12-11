from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from sisolo.decorators import admin_only
from sisolo.forms import Register
from sisolo.models import User
from django.views.decorators.csrf import csrf_exempt
import json

# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_mobile(request):
    body_unicode = (request.body.decode('utf-8'))
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    if username and password:
        User.objects.create(username=username, password=password)
    user = User (username = username, password = password)
    user.save()
    return JsonResponse({'status': 'Success'})

@csrf_exempt
def edit_user_mobile(request):
    body_unicode = (request.body.decode('utf-8'))
    user = User.objects.get(user=request.user)
    body = json.loads(body_unicode)
    namaLengkap = body['namaLengkap']
    nomorTeleponPemilik = body['nomorTeleponPemilik']
    alamatPemilik = body['alamatPemilik']
    user = User.objects.get(namaLengkap = namaLengkap, nomorTeleponPemilik = nomorTeleponPemilik, alamatPemilik = alamatPemilik)
    user.save()
    return HttpResponse(status=202)


def landing_page(request):
    if request.user.is_authenticated:
        data = User.objects.filter(user=request.user)
        context = {
            'user': request.user,
            'data': data,
        }
        return render(request, 'landing_page.html', context)
    else:
        return render(request, 'landing_page.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not User.objects.filter(user = request.user).exists():
                response = HttpResponseRedirect(reverse("sisolo:registerAddition"))
            else:
                if (User.objects.get(user = request.user).role == 'Admin'):
                    response = HttpResponseRedirect(reverse("Admin:show_admin_page"))
                else:
                    response = HttpResponseRedirect(reverse("sisolo:landing_page"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def login_user_mobile(request):
    body_unicode = (request.body.decode('utf-8'))
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    userTemp = authenticate(request, username=username, password=password)
    if userTemp is not None:
        if not User.objects.filter(user = userTemp).exists():
            return JsonResponse({'status':'notRegister'})
        else:
            userLogin = User.objects.get(user = userTemp)
            response = {
                'status':'register',
                'fields':{
                    'username':username,
                    'role':userLogin.role,
                    'namaLengkap':userLogin.namaLengkap,
                    'nomorTeleponPemilik':userLogin.nomorTeleponPemilik,
                    'alamatPemilik':userLogin.alamatPemilik,
                }
            }
            return JsonResponse(response)
    else:
        return JsonResponse({'status':'failed'})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('sisolo:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def registerAddition(request):
    form = Register()

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            namaLengkap = request.POST.get('namaLengkap')
            nomorTelepon = request.POST.get('nomorTelepon')
            alamat = request.POST.get('alamat')
            pengguna = User(user = request.user, nomorTeleponPemilik = nomorTelepon, alamatPemilik = alamat, namaLengkap = namaLengkap)
            pengguna.save()
            return redirect('sisolo:landing_page')
    
    context = {'form':form}
    return render(request, "registerAddition.html", context)

@login_required(login_url='/login/')
def editProfile(request):
    form = Register()

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = User.objects.get(user=request.user)
            user.namaLengkap = request.POST.get('namaLengkap')
            user.nomorTeleponPemilik = request.POST.get('nomorTelepon')
            user.alamatPemilik = request.POST.get('alamat')
            user.save()
            return redirect('sisolo:landing_page')
    
    context = {'form':form}
    return render(request, "registerAddition.html", context)

@login_required(login_url='/login/')
@admin_only
def all_user_data_json(request):
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('sisolo:landing_page'))
    return response
    
def logout_mobile(request):
    logout(request)
    response = HttpResponseRedirect(reverse('sisolo:login'))
    response.delete_cookie('last_login')
    return response