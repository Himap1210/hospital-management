from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField(max_length=100)
    
    def __str__(self):
        return self.dept_name
    
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to="doctors")
    
    def __str__(self):
        return 'DR' + self.doc_name+ '-('  +self.doc_spec+') ' 
    
class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_mail=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
class Contact(models.Model):
  p_name=models.CharField(max_length=255)
  p_email=models.EmailField()
  p_phone=models.CharField(max_length=10)
  p_message=models.CharField(max_length=255)
  contact_on=models.DateField(auto_now=True)