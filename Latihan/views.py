
from django.contrib import messages
from django.shortcuts import render
from Latihan.models import EmpModel

def index(request):
    showall=EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def insertemp(request):
    if request.method=="POST":
        if request.POST.get('Nama') and request.POST.get('Alamat') and request.POST.get('Email'):
            saverecord=EmpModel()
            saverecord.Nama=request.POST.get('Nama')
            saverecord.Alamat=request.POST.get('Alamat')
            saverecord.Email=request.POST.get('Email')
            saverecord.save()
            messages.success(request, 'Employee'+saverecord.Nama+ 'Sukses Menyimpan')
            return render(request, 'Insert.html')
    else:
            return render(request,'Insert.html')
