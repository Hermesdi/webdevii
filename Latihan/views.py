from django.contrib import messages
from django.shortcuts import render
from Latihan.models import EmpModel
from Latihan.forms import Empforms

def index(request):
    showall=EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def insertemp(request):
    if request.method=="POST":
        if request.POST.get('Nama') and request.POST.get('Alamat') and request.POST.get('Email'):
            saverecord=EmpModel()
            saverecord.nama=request.POST.get('Nama')
            saverecord.alamat=request.POST.get('Alamat')
            saverecord.email=request.POST.get('Email')
            saverecord.save()
            return render(request, 'Insert.html')
    else:
            return render(request,'Insert.html')
def Edit (request,id):
    editempobj=EmpModel.objects.get(id=id)
    return render (request,'Edit.html',{"EmpModel":editempobj})

def update (request,id):
    Updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        return render (request,'Edit.html',{"EmpModel":Updateemp})


def delete (request,id):
    delemployee = EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request,"Index.html", {"data":showdata})