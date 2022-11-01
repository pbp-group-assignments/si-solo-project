from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from sisolo.forms import Register
from sisolo.models import User

def landing_page(request):
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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('sisolo:login_user'))
    return response
    