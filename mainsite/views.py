from django.shortcuts import render , redirect
from .models import *
from django.http import JsonResponse
# Create your views here.

def index(request):

    args = dict()

    fm = For_me.objects.filter(avail= True)

    if len(fm) == 0 :
        fm = False
    else:
        fm = fm[0]
    args['fm'] = fm

    parthers = Partners.objects.filter(avail= True)

    if len(parthers) == 0 :
        parthers = False

    keys = Keys.objects.filter(available= True)

    if len(keys) == 0 :
        keys = False

    args['fm'] = fm
    args['pts'] = parthers
    args['keys'] = keys
    args['contakts'] = Contakts.objects.filter(available= True)

    return render(request, "index.html",args)

def aboyt_keus(request,slug):

    return render(request, "keys_podrob.html" , {'keys':Keys.objects.filter(slug= slug)[0] , 'mor_img':Images_keys.objects.filter(product_id = Keys.objects.filter(slug= slug)[0].id)})

def nevs(request):

    arg = dict()
    arg['news'] = Nevs.objects.filter(available= True)
    arg['mo_photo'] = Images_nevs.objects.all()
    return render(request, "nevsV2.html",arg)

def add_zap(request):

    try:
        zai = Zaiavki()

        zai.name = request.GET.get('name')
        zai.svaz = request.GET.get('svaz')
        zai.description = request.GET.get('opis')
        zai.status = "Непрочитанно"
        zai.available = True

        zai.save()

        return JsonResponse({"flag":True})
    except:

        return JsonResponse({"flag": False})