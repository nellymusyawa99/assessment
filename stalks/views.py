from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from stalks.models import merchandise



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
        merchandisename = request.POST.get('merchandisename')
        merchandisetype = request.POST.get('merchandisetype')
        merchandiseamount = request.POST.get('merchandiseamount')

        obj1 = stalks(merchandisename=merchandisename,merchandisetype=merchandisetype,merchandiseamount=merchandiseamount)
        obj1.save()

        mydata = merchandise.objects.all()
        context = {"data": mydata}
    return render(request,"stalks.html",context)


def updatestalks(request,id):
    if request.method == 'POST':
        merchandisename = request.POST.get('merchandisename')
        merechandisetype = request.POST.get('merchandisetype')
        merchandiseamount = request.POST.get('merchandiseamount')


        #modifying the student details based on the student id given
        updatestalks = merchandise.objects.get(id=id)#here i fetch the student to be changed
        updatestalks.merchandisename = merchandisename
        updatestalks.merchandisetype = merechandisetype
        updatestalks.merchandiseamount = merchandiseamount
        #save the changes
        updatestalks.save()
        #display the new changes in html table to fetch them from the database table
        data = merchandise.objects.all()
        #i create a dictionary to hold the fetched info
        context = {'data': data}
        #pass the fetched info back to the dashboard
    return render(request, 'stalks.html',context)


def deletestalks(request,id):
    deletestalks = merchandise.objects.get(id=id)
    deletestalks.delete()
    return redirect('/stalks')
# Create your views here