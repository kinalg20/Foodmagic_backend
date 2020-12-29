import random
from django.db import models
# from address.models import Address
# from restaurants.models import Restaurants

def random_id_genrate():
    return random.randint(1,3910209312)

# Customer
class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True,default=random_id_genrate,unique=True)
    profile_photo=models.ImageField(upload_to='users_profiles/',null=True, blank=True)
    first_name=models.CharField(max_length=50,default="",null=False, blank=True)
    last_name=models.CharField(max_length=50,default="",null=False, blank=True)
    # address=models.ForeignKey(Address,on_delete=models.CASCADE,related_name='customer_address',null=True,blank=True)
    phone_number=models.CharField(max_length=12,null=False,blank=True)
    email_id=models.EmailField(verbose_name='email_address',max_length=255,unique=True)
    is_seller=models.BooleanField(default=False)
    is_deliveryBoy=models.BooleanField(default=None)


#seller
class Seller(models.Model):
    seller_id=models.AutoField(primary_key=True,default=random_id_genrate)
    customer_id=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='Restaurant_seller',null=True,blank=True)
    phone_number=models.CharField(max_length=12,null=True,blank=True)
    back_ac_number=models.CharField(max_length=12,null=True,blank=True)
    ac_holder_name=models.CharField(max_length=55)
    ifsc_code=models.CharField(max_length=11,null=True,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.seller_id)
    def name(self):
        return str(self.customer_id.first_name)+""+str(self.customer_id.last_name)


#deliveryboy
class DeliveryBoy(models.Model):
    Delivery_boy_id=models.AutoField(primary_key=True,default=random_id_genrate)
    customer_id=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='restaurant_delivery_boy',null=True,blank=True)
    # restaurant_id=models.ForeignKey(Restaurants,on_delete=models.CASCADE,related_name='delivery_boy_restaurant',null=True,blank=True)
    delivery_charge=models.FloatField(blank=True,null=True)
    is_available=models.BooleanField(default=False)

    def __str__(self):
        return str(self.Delivery_boy_id)

    def joining_date(self):
        return self.customer_id.date_joined
    
    def delivery_cost(self):
        return self.delivery_charge

