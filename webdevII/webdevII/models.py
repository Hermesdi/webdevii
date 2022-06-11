from django.db import models

class EmpModel (models.Model):
    nama=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    alamat=models.CharField(max_length=100)
    class Meta:
        db_table= "employee"
