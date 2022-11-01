from django.shortcuts import render
from info_kebutuhan_pokok import Kebutuhan_Pokok
# Create your views here.

def show_kebutuhanpokok(request):
    data_kebutuhan = Kebutuhan_Pokok.objects.all()
    context = {

    }
    return render (request, "kebutuhan.html", context)
