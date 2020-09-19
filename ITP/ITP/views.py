from io import BytesIO

from xhtml2pdf import pisa
from django.shortcuts import render
from django.template.loader import get_template

from .models import ChargeInsert
from django.contrib import messages
from django.http import HttpResponse
from .forms import chargeform

def displaycharge(request):
    results=ChargeInsert.objects.all()
    return render(request,"display.html",{"ChargeInsert":results})

def Insertcharge(request):
    if request.method=='POST':

        if request.POST.get('servicename') and request.POST.get('charge') and request.POST.get('category'):
            saverecord=ChargeInsert()
            #saverecord.servicecode=request.POST.get('id')
            saverecord.servicename = request.POST.get('servicename')
            saverecord.charge = request.POST.get('charge')
            saverecord.category = request.POST.get('category')
            saverecord.save()
            messages.success(request,'Record saved successfully..!')
            return  render(request,'Index.html')
        else:
            return render(request,'Index.html')
    else:
        return render(request, 'Index.html')


def editcharge(request,id):
    getchargedetails=ChargeInsert.objects.get(id=id)
    return render(request,'edit.html',{"ChargeInsert":getchargedetails})

def chargeupdate(request,id):
    chargeupdate=ChargeInsert.objects.get(id=id)
    form=chargeform(request.POST,instance=chargeupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"Service Details  Updated Successfully..!")
        return render(request,"edit.html",{"ChargeInsert":chargeupdate})


def chargedelete(request,id):
    delcharge=ChargeInsert.objects.get(id=id)
    delcharge.delete()
    results = ChargeInsert.objects.all()
    return render(request, "display.html", {"ChargeInsert": results})


def getpdfPage(request):

    rec = ChargeInsert.objects.all()
    data = {'working': rec}
    template = get_template("pdfpage.html")
    data_p = template.render(data)
    response = BytesIO()
    pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")), response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")
