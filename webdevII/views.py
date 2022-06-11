from django.shortcuts import render
from webdevII.models import EmpModel
from webdevII.forms import Empforms

def showemp(request):
    showall=EmpModel.objects.all()
    return render (request,'Index.html',{"data":showall})

def insertemp(request):
    if request.method=="POST":
        if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('email'):
            saverecord=EmpModel()
            saverecord.nama=request.POST.get('nama')
            saverecord.alamat=request.POST.get('alamat')
            saverecord.email=request.POST.get('email')
            saverecord.save()
            return render(request, 'Insert.html')
    else:
            return render(request,'Insert.html')
        
def editemp(request,id):
    editempoj=EmpModel.objects.get(id=id)
    return render(request, 'Edit.html',{"EmpModel": editempoj})

def updateemp(request,id):
    Updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        return render(request,'Edit.html',{"EmpModel": Updateemp})
    
def delete(request,id):
    Dlt=EmpModel.objects.get(id=id)
    Dlt.delete()
    showdata=EmpModel.objects.all()
    return render(request,"Index.html",{"data":showdata})