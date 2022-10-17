from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def landing_page(request):
    return render(request, 'landing_page.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('sisolo:login_user'))
    return response

def daftar_pelaku_usaha(request):
    return render(request, 'daftar_pelaku_usaha.html')

def ubah_group_pengguna(request):
    print('masuk')
    request.user.groups = 'Pengguna'
    return redirect('pendaftaran_izin_usaha:show_pendaftaran')
    