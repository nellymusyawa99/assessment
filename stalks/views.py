from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import merchandise as MerchandiseModel  # Rename the merchandise model

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def merchandise(request):
    template = loader.get_template('merchandise.html')
    return HttpResponse(template.render())

def stalks(request):
    merchandise_items = MerchandiseModel.objects.all()
    context = {'merchandise_items': merchandise_items}
    return render(request, 'stalks.html', context)

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

@csrf_exempt
def addStalks(request):
    if request.method == 'POST':
        merchandise_name = request.POST.get('merchandisename')
        merchandise_type = request.POST.get('merchandisetype')
        merchandise_amount = request.POST.get('merchandiseamount')

        obj1 = MerchandiseModel.objects.create(merchandisename=merchandise_name, merchandisetype=merchandise_type, merchandiseamount=merchandise_amount)

        mydata = MerchandiseModel.objects.all()
        context = {"data": mydata}
        return render(request, "stalks.html", context)

    return HttpResponse("This view is for POST requests only.")



def updatestalks(request, id):
    if request.method == 'POST':
        merchandise_name = request.POST.get('merchandisename')
        merchandise_type = request.POST.get('merchandisetype')
        merchandise_amount = request.POST.get('merchandiseamount')

        try:
            update_stalks = MerchandiseModel.objects.get(id=id)
        except MerchandiseModel.DoesNotExist:
            return HttpResponse("Merchandise with this ID does not exist.", status=404)

        update_stalks.merchandisename = merchandise_name
        update_stalks.merchandisetype = merchandise_type
        update_stalks.merchandiseamount = merchandise_amount
        update_stalks.save()

        updated_data = MerchandiseModel.objects.all()
        context = {'data': updated_data}
        return render(request, 'stalks.html', context)

    else:
        return HttpResponse("This view is for POST requests only.", status=405)


def deletestalks(request, id):
    try:
        merchandise_instance = MerchandiseModel.objects.get(id=id)
        merchandise_instance.delete()
    except MerchandiseModel.DoesNotExist:
        return HttpResponse("The merchandise you are trying to delete does not exist.")

    return redirect('stalks')  # Redirect to the 'stalks' URL pattern