from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()
    def __str__(self):
        return self.dep_name
    
class Doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    dep_names=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name + ' - '+ self.doc_spec
    
class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.p_name