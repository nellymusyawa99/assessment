from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import user


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def merchandise(request):
    template = loader.get_template('merchandise.html')
    return HttpResponse(template.render())

def stalks(request):
    template = loader.get_template('stalks.html')
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

@csrf_exempt
def addstalks(request):
    if request.method == 'POST':
        merchandisename = request.POST('merchandisename')
        merchandisetype = request.POST('merchandisetype')
        merchandiseamount = request.POST('merchandiseamount')

        obj1=stalks(merchandisename=merchandisename,merchandisetype=merchandisetype,merchandiseamount=merchandiseamount)
        obj1=save()

        mydata = user.objects.all()
        context = {"data": mydata}


        return render(request,"stalks.html",context)


# Create your views here