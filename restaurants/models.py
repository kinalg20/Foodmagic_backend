from django.db import models
from address.models import Address
from accounts.models import Seller
from accounts.models import DeliveryBoy
# from accounts.models import Customers
import random
def random_id_genrate():
    return random.randint(1,3910209312)
# Create Restaurants here.
class Restaurants(models.Model):
    restaurant_id=models.AutoField(primary_key=True,default=random_id_genrate)
    restaurant_name=models.CharField(max_length=100,default="",null=True,blank=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,related_name='restaurant_address',null=True,blank=True)
    logo_img=models.FileField(upload_to='restaurants/logos/',null=True,blank=True)
    seller_id=models.ForeignKey(Seller,on_delete=models.CASCADE,null=True,blank=True)
    cover_image=models.FileField(upload_to='restaurants/cover_images/',null=True,blank=True)
    cuisines=models.TextField(max_length=255)
    min_order_amt=models.FloatField()
    foodmagic_pro=models.BooleanField(blank=False,null=False,default=False)
    Opening_time=models.DateTimeField(null=False,blank=False)
    closing_time=models.DateTimeField(null=False,blank=False)
    desc=models.TextField(max_length=255)
    today_off=models.BooleanField(blank=False,null=False,default=False)
    joining_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.restaurant_id)

    def restaurant_address(self):
        return str(self.address)

    
