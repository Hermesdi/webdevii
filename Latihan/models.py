from django.db import models

class EmpModel (models.Model):
    Nama=models.CharField(max_length=100)
    Alamat=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    class Meta:
        db_table= "employee"