from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from berita_isu_terkini.forms import Create
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# Create your views here.
from berita_isu_terkini.models import Berita
from sisolo.decorators import admin_only

# def show_berita(request):
#     berita_terkini = Berita.objects.all()
#     context = {
#         'list_berita' : berita_terkini,
#     }
#     return render (request, "beritaterkini.html", context)

def show_berita(request):
    if is_ajax(request=request) : 
        p = Berita(news_title='Test', news_description='Berkeley', news_highlight='Data baru', image_url='https://filestore.community.support.microsoft.com/api/images/371db990-f99c-49e3-a230-c7de0458f791?upload=true')
        p.save()
        context = Berita.objects.all().values()
        arr = []
        for i in context :
            arr += [i]
        return JsonResponse(arr, safe=False)
    else :
        return render(request, "beritaterkini.html", {})

def show_berita_json(request):
    data = Berita.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# @login_required(login_url='/login/')
# @admin_only
# def show_create(request):
#     #user = request.user
#     form = Create()
#     if request.method == 'POST':
#         form = Create(request.POST, request.FILES)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#         #Task.objects.create(user_id=user.id, title=title, description=description, date=date)
#             return redirect ('todolist:show_todolist')
#         else:
#             form = Create(initial={'user': request.user})
#     context = {'form':form}
#     return render(request, 'create.html', context)
