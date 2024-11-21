from django.db import models

# Create your models here.
class Customer(models.Model):
    image = models.ImageField(upload_to='customers_images/',blank=True)
    name = models.CharField(max_length=20)
    admissionNumber = models.IntegerField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=11)
    age = models.IntegerField()

    def __str__(self):
        return self.name