from django.db import models
# from accounts.models import Customer
# Create your models here.
import random
def random_id_genrate():
    return random.randint(1,3910209312)

class Address(models.Model):
    region=models.CharField(max_length=50,default="")
    country=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    area=models.CharField(max_length=50,default="")
    zip_code=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=50,default="")



    # def __str__(self):
    #     full_address=((self.area)+(self.city)+", "(self.state)+"("(self.zip_code)+")- "(self.country)+(self.Address_id))
    #     return full_address



